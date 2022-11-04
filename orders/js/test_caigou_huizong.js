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

var cg_table = informat.table.getTable("采购明细");
var cg_fieldList = informat.table.getFieldList(cg_table.id);
var cg_sku_codeField = getField(cg_fieldList, "SKU编码");
var cg_p_price_codeField = getField(cg_fieldList, "计划单价");
var cg_p_count_codeField = getField(cg_fieldList, "计划数量");
var cg_o_price_codeField = getField(cg_fieldList, "下单单价");
var cg_o_count_codeField = getField(cg_fieldList, "下单数量");
var cg_s_price_codeField = getField(cg_fieldList, "实际单价");
var cg_s_count_codeField = getField(cg_fieldList, "实际数量");
var cg_type_codeField = getField(cg_fieldList, "订单类型");

// console.log(recorder);

const sku_code = recorder["变量值"]["SKU编码"];
var resp = informat.table.query(cg_table.id, {
  includeFields: [
    cg_sku_codeField.id,
    cg_p_price_codeField.id,
    cg_p_count_codeField.id,
    cg_o_price_codeField.id,
    cg_o_count_codeField.id,
    cg_s_price_codeField.id,
    cg_s_count_codeField.id,
    cg_type_codeField.id,
  ],
  conditionList: [
    { fieldId: cg_sku_codeField.id, opt: "eq", value: sku_code },
    { fieldId: cg_type_codeField.id, opt: "eq", value: "ex43n6ru49jv" },
  ],
});
//console.log(resp);

const data = resp.list;

let s_data = { p: {}, o: {}, s: {}, p_count: 0, o_count: 0, s_count: 0 };

for (let index = 0; index < data.length; index++) {
  let item = data[index];
  let p_price = item[cg_p_price_codeField.id];
  let p_count = item[cg_p_count_codeField.id];
  let o_price = item[cg_o_price_codeField.id];
  let o_count = item[cg_o_count_codeField.id];
  let s_price = item[cg_s_price_codeField.id];
  let s_count = item[cg_s_count_codeField.id];
  let type = item[cg_type_codeField.id];

  if (s_data.p[p_price] == undefined) {
    s_data.p[p_price] = p_count;
  } else {
    s_data.p[p_price] += p_count;
  }
  if (s_data.o[o_price] == undefined) {
    s_data.o[o_price] = o_count;
  } else {
    s_data.o[o_price] += o_count;
  }

  if (s_data.s[s_price] == undefined) {
    s_data.s[s_price] = s_count;
  } else {
    s_data.s[s_price] += s_count;
  }
  s_data.p_count += p_count;
  s_data.s_count += s_count;
  s_data.o_count += o_count;
}

// console.log(s_data);

var hz_table = informat.table.getTable("采购汇总");
var hz_fieldList = informat.table.getFieldList(hz_table.id);
var hz_sku_codeField = getField(hz_fieldList, "SKU编码");
var hz_p_price_count_codeField = getField(hz_fieldList, "计划单价数量");
var hz_o_price_count_codeField = getField(hz_fieldList, "下单单价数量");
var hz_s_price_count_codeField = getField(hz_fieldList, "到库单价数量");
var hz_p_count_codeField = getField(hz_fieldList, "计划总数");
var hz_o_count_codeField = getField(hz_fieldList, "下单总数");
var hz_s_count_codeField = getField(hz_fieldList, "到库总数");
var resp = informat.table.query(hz_table.id, {
  includeFields: [
    hz_sku_codeField.id,
    hz_p_price_count_codeField.id,
    hz_o_price_count_codeField.id,
    hz_s_price_count_codeField.id,
    hz_p_count_codeField.id,
    hz_o_count_codeField.id,
    hz_s_count_codeField.id,
  ],
  conditionList: [{ fieldId: hz_sku_codeField.id, opt: "eq", value: sku_code }],
});

let bean = {
  SKU编码: sku_code,
  计划单价数量: Object.keys(s_data.p)
    .map((k) => k + "/" + s_data.p[k])
    .join(","),
  下单单价数量: Object.keys(s_data.o)
    .map((k) => k + "/" + s_data.o[k])
    .join(","),
  到库单价数量: Object.keys(s_data.s)
    .map((k) => k + "/" + s_data.s[k])
    .join(","),
  计划总数: s_data.p_count,
  下单总数: s_data.o_count,
  到库总数: s_data.s_count,
};
console.log({ bean, resp });
if (resp.count == 0) {
  bean = informat.table.convert(hz_fieldList, bean);
  const val = informat.table.insert(hz_table.id, bean);
} else {
  bean = informat.table.convert(hz_fieldList, bean);
  const val = informat.table.update(hz_table.id, resp.list[0].id, bean);
}
