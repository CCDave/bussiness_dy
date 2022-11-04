var table_id = "1Z4y4y3GGhYTuh1F";

// 计算项
// 订单ID
var order_id = "1Z4y4y3GHcPw2RzX";
// 商品价格
var p_price = "1Z4y4y3GHsR4YIQV";
// 商品数量
var p_count = "1Z4y4y3GI4pl1MYB";
// 结算金额
var settle_amount = "1Z4y4y3HEEk8yPlY";
// 收入合计
var total_income = "1Z4y4y3HEEsK7wq5";
// 平台服务费
var platform_service_amount = "1Z4y4y3HEEA4u4d3";
// 支出合计
var total_expend = "1Z4y4y3HEEMgEE8x";
// 手续费
var service_charge = "1Z4y4y3HEEVy8WWF";

//筛选项
// 商品id
var p_id = "1Z4y4y3GI4easoPw";
// 订单阶段
var r_order_status = "1Z4y4y3HEF2bMVrg";
// 结算阶段
var r_order_settle_status = "1Z4y4y3HEF7PMuRf";
// 完整SKU编码
var s_sku_finish_code = "1Z4y4y3HESycnFHU";
// 供应商
var s_supplier = "1Z4y4y3HESG5qDSt";
// 订单提交日期
var order_submit_date = "1Z4y4y3GI5CHuPUy";
// 订单结算日期
var settle_date = "1Z4y4y3HEE555CMj";
// 几天发货
var express_delivery_days = "1Z4y4y3HEBaaU5lJ";
// 几天退款
var refund_days = "1Z4y4y3H1hAyslAJ";
// 几天结算
var settle_days = "1Z4y4y3HEEcaT7RS";

console.log({
  table_id,
  order_id,
  p_price,
  // 筛选项
  p_id,
  r_order_status,
  r_order_settle_status,
  s_sku_finish_code,
  s_supplier,
  order_submit_date,
  settle_date,
  // 计算
});
var content =
  "| 名称                    | 类型   | 必填 | 备注           | \n" +
  "| ----------------------- | ------ | ---- | -------------- |\n" +
  "| tableId                 | String | 是   | 数据表ID       |\n" +
  "| fieldId                 | String | 是   | 字段ID         |\n" +
  "|content                  | String | 是   | 富文本原始内容 |";

function show_log(params) {
  var content =
    "| 参数                    | 类型   | 必填 | 备注           | \n" +
    "| ----------------------- | ------ | ---- | -------------- |\n";

  for (let i = 0; i < params.length; i++) {
    content +
      "|" +
      params[i] +
      "                 | String | 是   | 数据表ID       |\n";
  }
  content += "|content                  | String | 是   | 富文本原始内容 |";
  dashboard.setMarkdownOption(params[0] + "<br>\n\n" + content);
}
const product_id = dashboard.getParameter("商品ID");
const full_sku_code = dashboard.getParameter("SKU");
const start_date = dashboard.getParameter("下单日期-开始");
const end_date = dashboard.getParameter("下单日期-结束");
const supply = dashboard.getParameter("供应商");
show_log([product_id, full_sku_code, start_date, end_date, supply]);

const conditionList = [];
if (product_id != "") {
  conditionList.append({ fieldId: p_id, opt: "eq", value: product_id });
}
if (full_sku_code != "") {
  conditionList.append({
    fieldId: s_sku_finish_code,
    opt: "contains",
    value: full_sku_code,
  });
}

if (start_date != "" && end_date != "") {
  conditionList.append({
    filter: {
      opt: "or",
      conditionList: [
        { fieldId: order_submit_date, opt: "ge", value: start_date },
        { fieldId: order_submit_date, opt: "le", value: end_date },
      ],
    },
  });
} else if (
  (start_date != "" && end_date == "") ||
  (start_date == "" && end_date != "")
) {
  conditionList.append({
    fieldId: order_submit_date,
    opt: "eq",
    value: start_date == "" ? end_date : start_date,
  });
}
if (supply != "") {
  conditionList.append({
    fieldId: s_supplier,
    opt: "eq",
    value: supply,
  });
}

let query_set = {
  useFieldName: true,
  groupByFieldList: [
    p_id,
    r_order_status,
    r_order_settle_status,
    s_sku_finish_code,
    s_supplier,
    order_submit_date,
    settle_date,
  ],
  aggregationQueryList: [{ field: order_id, func: "count", distinct: false }],
};
if (conditionList.length > 0) {
  query_set.conditionList = conditionList;
}

var resp = informat.table.query(table_id, query_set);
console.log(resp);
