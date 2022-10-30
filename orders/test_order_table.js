function show_log(params) {
  var content =
    "| 参数                    | 类型   | 必填 | 备注           | \n" +
    "| ----------------------- | ------ | ---- | -------------- |\n";

  for (let i = 0; i < params.length; i++) {
    content += `| ${params[i]}            | String | 是   | 数据表ID       |\n`;
  }
  content += "|content                  | String | 是   | 富文本原始内容 |";
  dashboard.setMarkdownOption(
    `参数：${JSON.stringify(params)}` + "<br>\n\n" + content
  );
  //console.log(params);
}
const ids = {
  table_id: "1Z4y4y3GGhYTuh1F", // 计算项
  // 订单ID
  order_id: "1Z4y4y3GHcPw2RzX",
  // 商品价格
  p_price: "1Z4y4y3GHsR4YIQV",
  // 商品数量
  p_count: "1Z4y4y3GI4pl1MYB",
  // 结算金额
  settle_amount: "1Z4y4y3HEEk8yPlY",
  // 订单应付金额
  payable: "1Z4y4y3GI5SYeLhx",
  // 收入合计
  total_income: "1Z4y4y3HEEsK7wq5",
  // 平台服务费
  platform_service_amount: "1Z4y4y3HEEA4u4d3",
  // 支出合计
  total_expend: "1Z4y4y3HEEMgEE8x",
  // 手续费
  service_charge: "1Z4y4y3HEEVy8WWF",

  //筛选项
  // 商品id
  p_id: "1Z4y4y3GI4easoPw",
  // 订单阶段
  r_order_status: "1Z4y4y3HEF2bMVrg",
  // 结算阶段
  r_order_settle_status: "1Z4y4y3HEF7PMuRf",
  // 完整SKU编码
  s_sku_finish_code: "1Z4y4y3HESycnFHU",
  // 供应商
  s_supplier: "1Z4y4y3HESG5qDSt",
  // 订单提交日期
  order_submit_date: "1Z4y4y3GI5CHuPUy",
  // 订单结算日期
  settle_date: "1Z4y4y3HEE555CMj",
  // 几天发货
  express_delivery_days: "1Z4y4y3HEBaaU5lJ",
  // 几天退款
  refund_days: "1Z4y4y3H1hAyslAJ",
  // 几天结算
  settle_days: "1Z4y4y3HEEcaT7RS",
};

const product_id = dashboard.getParameter("商品ID");
const full_sku_code = dashboard.getParameter("SKU");
const start_date = dashboard.getParameter("开始日期");
const end_date = dashboard.getParameter("结束日期");
const supply = dashboard.getParameter("供应商");

const filter = {
  opt: "and",
  conditionList: [],
};

if (product_id != null) {
  filter.conditionList.push({
    fieldId: ids.p_id,
    opt: "eq",
    value: product_id,
  });
}
if (full_sku_code != null) {
  filter.conditionList.push({
    fieldId: ids.s_sku_finish_code,
    opt: "contains",
    value: full_sku_code,
  });
}

if (start_date != null && end_date != null) {
  filter.conditionList.push({
    fieldId: ids.order_submit_date,
    opt: "ge",
    value: start_date,
  });
  filter.conditionList.push({
    fieldId: ids.order_submit_date,
    opt: "le",
    value: end_date,
  });
} else if (
  (start_date != null && end_date == null) ||
  (start_date == null && end_date != null)
) {
  filter.conditionList.push({
    fieldId: ids.order_submit_date,
    opt: "eq",
    value: start_date == null ? end_date : start_date,
  });
}
if (supply != null) {
  filter.conditionList.push({
    fieldId: ids.s_supplier,
    opt: "eq",
    value: supply,
  });
}
let query_set = {
  useFieldName: true,
  groupByFieldList: [ids.r_order_status],
  aggregationQueryList: [
    { field: ids.order_id, func: "count", distinct: false },
    { field: ids.p_count, func: "count", distinct: false },
    { field: ids.settle_amount, func: "sum", distinct: false },
    { field: ids.total_income, func: "sum", distinct: false },
    { field: ids.platform_service_amount, func: "sum", distinct: false },
    { field: ids.total_expend, func: "sum", distinct: false },
    { field: ids.service_charge, func: "sum", distinct: false },
    { field: ids.payable, func: "sum", distinct: false },
  ],
};
if (filter.conditionList.length > 0) {
  query_set.filter = filter;
}
var resp = informat.table.query(ids.table_id, query_set);
// 总订单数
// 未支付数
// 支付数
// 发货前退款
// 发货后退款
// 所有退款
// 待结算订单数
// 待结算金额
// 已计算订单数
// 已经结算金额
/*
"结算金额_求和"
"订单阶段": "已发货", 未付款 发货前退款 发货后退款 已发货 备货中
"结算阶段": "反结算",

"子订单编号_数量"
"订单应付金额_求和"
"收入合计_求和"
"手续费_求和"
"商品数量_数量"
"平台服务费_求和"
"支出合计_求和"
*/
var datas = resp.list;

function getValueByPairs(collect, c_key, c_value, value) {
  return collect.sum((product) =>
    product[c_key] == c_value ? product[value] : 0
  );
}

const collect_s = collect(datas);
let s = collect_s;
var total_orders = s.sum("子订单编号_数量");
var no_pay_orders = getValueByPairs(s, "订单阶段", "未付款", "子订单编号_数量");
var refund_before = getValueByPairs(
  s,
  "订单阶段",
  "发货前退款",
  "子订单编号_数量"
);
var refund_after = getValueByPairs(
  s,
  "订单阶段",
  "发货后退款",
  "子订单编号_数量"
);
var delivery = getValueByPairs(s, "订单阶段", "已发货", "子订单编号_数量");
var delivery_amount = getValueByPairs(
  s,
  "订单阶段",
  "已发货",
  "订单应付金额_求和"
);
var prepare = getValueByPairs(s, "订单阶段", "备货中", "子订单编号_数量");
var prepare_amount = getValueByPairs(
  s,
  "订单阶段",
  "备货中",
  "订单应付金额_求和"
);
var pay_count = total_orders - no_pay_orders;
var total_refund = refund_after + refund_before;
var waite_settle = delivery + prepare;
var waite_settle_mount = delivery_amount + prepare_amount;
var pay_percent = (1 - no_pay_orders / total_orders).toFixed(2);
var refund_percent = (total_refund / pay_count).toFixed(2);
var waite_settle_percent = (waite_settle / pay_count).toFixed(2);
var before_percent = (refund_before / pay_count).toFixed(2);
var after_percent = (refund_after / pay_count).toFixed(2);
var content =
  "|渠道|订单数|未付款|付款率|发前退款|发前退款率|发后退款|发后退款率|未支付/退款|退款率|已发货|备货中|待结算|待结算比例|待结算金额\n" +
  "|---|------|----- |-----|-------|---------|--------|---------|----------|------|-----|------|-----|--------|--------| \n";
content += `|总数| ${total_orders}|${no_pay_orders}|${pay_percent}|${refund_before}|${before_percent}|${refund_after}|${after_percent}|${total_refund}|${refund_percent}|${delivery}|${prepare} |${waite_settle} |${waite_settle_percent}|${waite_settle_mount} |\n`;

dashboard.setMarkdownOption(content);
