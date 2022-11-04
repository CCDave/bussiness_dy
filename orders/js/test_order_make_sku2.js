const db_url = "jdbc:postgresql://121.41.19.35:5432/postgres";
const db_user = "postgres";
const db_password = "SRwHwWnL24kAwsDs";
const db_class_name = "org.postgresql.Driver";

function getField(fieldList, name) {
  return fieldList.find((f) => f.name == name);
}

function query(sql, params) {
  let data = {
    dburl: db_url,
    dbuser: db_user,
    dbpassword: db_password,
    driverClassName: db_class_name,
    sql: sql,
  };
  if (params !== null) {
    data.parameters = params;
  }
  console.log(data);
  return informat.jdbc.queryList(data);
}

function update(sql, params) {
  let data = {
    dburl: db_url,
    dbuser: db_user,
    dbpassword: db_password,
    driverClassName: db_class_name,
    sql: sql,
  };
  if (params !== null) {
    data.parameters = params;
  }
  console.log(data);
  return informat.jdbc.executeUpdate(data);
}

var supply_table = informat.table.getTable("供应商管理");
var supply_fieldList = informat.table.getFieldList(supply_table.id);
var supply_supply_codeField = getField(supply_fieldList, "商家编码");
var supply_nameField = getField(supply_fieldList, "名称");

var sku_table = informat.table.getTable("SKU对照表");
var sku_fieldList = informat.table.getFieldList(sku_table.id);
var sku_sku_codeField = getField(sku_fieldList, "SKU编码");
var sku_supplyField = getField(sku_fieldList, "供应商");

console.log(updaterecord);
const p_code = updaterecord["变量值"]["货号"];
const color = updaterecord["变量值"]["颜色尺码"];
const p_id = updaterecord["变量值"]["商品ID"];
const recode_id = updaterecord["变量值"]["id"];
let supply_name = null;
let sku_code_finish = null;
if (p_code != undefined && p_code != "" && p_code != null) {
  // 取货号
  if (p_code.indexOf("-") != -1) {
    const supply_code = p_code.split("-")[0];
    var resp = informat.table.query(supply_table.id, {
      includeFields: [supply_supply_codeField.id, supply_nameField.id],
      conditionList: [
        { fieldId: supply_supply_codeField.id, opt: "eq", value: supply_code },
      ],
    });
    if (resp.count != 0) {
      let q_data = resp.list[0];
      supply_name = q_data[supply_nameField.id];
    }
    sku_code_finish = p_code + "-" + color;
    var bean = {
      SKU编码: sku_code_finish,
    };
    if (supply_name !== null) {
      bean["供应商"] = supply_name;
    }
    bean = informat.table.convert(sku_fieldList, bean);
    informat.table.update(sku_table.id, recode_id, bean);
  }

  if (
    p_id != null &&
    color != null &&
    (supply_name != null || sku_code_finish != null)
  ) {
    console.log({ p_id, color, supply_name, sku_code_finish });
    const sql = `update "OrdersModel_orders" set "s_sku_finish_code"=?, "s_supplier"=? where "p_id"=? and "sku_code"=? `;
    const parameters = [sku_code_finish, supply_name, p_id, color];
    const ret = update(sql, parameters);
    console.log(ret);
  }
}
