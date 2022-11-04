const db_url = "jdbc:postgresql://121.41.19.35:5432/postgres";
const db_user = "postgres";
const db_password = "SRwHwWnL24kAwsDs";
const db_class_name = "org.postgresql.Driver";

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
  return informat.jdbc.executeUpdate(data);
}
const q_sku = query(
  `select "sku_code","p_id" from "OrdersModel_orders" group by "sku_code","p_id"`,
  null
);
// console.log(q_sku);
let sku_s = {};

for (let i in q_sku) {
  let item = q_sku[i];
  // console.log(item);
  if (sku_s[item["p_id"]] == undefined) {
    sku_s[item["p_id"]] = [item["sku_code"]];
  } else {
    sku_s[item["p_id"]].push(item["sku_code"]);
  }
}
function getField(fieldList, name) {
  return fieldList.find((f) => f.name == name);
}

var table = informat.table.getTable("SKU对照表");
var fieldList = informat.table.getFieldList(table.id);

var fixField = getField(fieldList, "SKU拼接");
var pidField = getField(fieldList, "商品ID");
var supplyField = getField(fieldList, "供应商");
var sku_code_finishField = getField(fieldList, "SKU编码");

for (let p_id in sku_s) {
  for (let index in sku_s[p_id]) {
    // 按条插入
    let c_cku = sku_s[p_id][index];
    let sku_p = p_id + c_cku;
    var resp = informat.table.query(table.id, {
      includeFields: [
        fixField.id,
        pidField.id,
        supplyField.id,
        sku_code_finishField.id,
      ],
      conditionList: [{ fieldId: fixField.id, opt: "eq", value: sku_p }],
    });
    if (resp.count == 0) {
      let bean = {
        SKU拼接: sku_p,
        颜色尺码: c_cku,
        商品ID: p_id,
      };
      bean = informat.table.convert(fieldList, bean);
      const val = informat.table.insert(table.id, bean);
    } else {
      // 看看有啥编码把数据库编码做上
      let q_data = resp.list[0];
      let supply = q_data[supplyField.id];
      let sku_code_finish = q_data[sku_code_finishField.id];
      if (supply != undefined || sku_code_finish != undefined) {
        // 更新数据库数据
        //`select "sku_code","p_id" from "OrdersModel_orders" group by "sku_code","p_id"`
        const sql = `update "OrdersModel_orders" set "s_sku_finish_code"=?, "s_supplier"=? where "p_id"=? and "sku_code"=? and ("s_sku_finish_code"!=? or "s_supplier"!=?)`;
        const parameters = [
          sku_code_finish,
          supply,
          p_id,
          c_cku,
          sku_code_finish,
          supply,
        ];
        const ret = update(sql, parameters);
        console.log(ret);
      }
    }
  }
}

// console.log(sku_s);
