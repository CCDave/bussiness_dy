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
    { field: ids.p_count, func: "sum", distinct: false },
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
"商品数量_求和"
"平台服务费_求和"
"支出合计_求和"
*/
var datas = resp.list;
function getValueByPairs(collect, c_key, c_value, value) {
  return collect.sum((product) =>
    product[c_key] == c_value ? product[value] : 0
  );
}
function getValues(collect, c_key, c_vale, p_total) {
  var obj = {
    order_count: 0,
    need_pay_mount: 0,
    p_count: 0,
    settle_amount: 0,
    percent: 0,
  };
  obj.order_count = getValueByPairs(collect, c_key, c_vale, "子订单编号_数量");

  obj.need_pay_mount = getValueByPairs(
    collect,
    c_key,
    c_vale,
    "订单应付金额_求和"
  );

  obj.p_count = getValueByPairs(collect, c_key, c_vale, "商品数量_求和");
  obj.settle_amount = getValueByPairs(collect, c_key, c_vale, "结算金额_求和");
  obj.percent = ((obj.order_count / p_total) * 100).toFixed(2);
  return obj;
}
const collect_s = collect(datas);
let s = collect_s;
var total_orders = s.sum("子订单编号_数量");

var total_amount = 0;
datas.filter(
  (f) => (total_amount += f["订单应付金额_求和"] ? f["订单应付金额_求和"] : 0)
);
total_amount = total_amount.toFixed(2);
var no_pay_orders = getValues(s, "订单阶段", "未付款", total_orders);

var pay_count = total_orders - no_pay_orders.order_count;
var pay_percent = (
  100 -
  (no_pay_orders.order_count / total_orders) * 100
).toFixed(2);
var pay_amount = total_amount;

var refund_before = getValues(s, "订单阶段", "发货前退款", pay_count);
var refund_after = getValues(s, "订单阶段", "发货后退款", pay_count);

var total_refund = refund_after.order_count + refund_before.order_count;
var total_refund_percent = ((total_refund / pay_count) * 100).toFixed(2);

var delivery = getValues(s, "订单阶段", "已发货", pay_count);

var prepare = getValues(s, "订单阶段", "备货中", pay_count);

var waite_settle = delivery.order_count + prepare.order_count;
var waite_settle_p_count = delivery.p_count + prepare.p_count;
var waite_settle_percent = ((waite_settle / pay_count) * 100).toFixed(2);
var waite_settle_mount = delivery.need_pay_mount + prepare.need_pay_mount;

var settle = getValues(s, "订单阶段", "已结算", pay_count);

var r_settle = getValues(s, "订单阶段", "反结算", pay_count);

var platform_service_amount = 0;
datas.filter(
  (f) =>
    (platform_service_amount += f["平台服务费_求和"] ? f["平台服务费_求和"] : 0)
);

var deliver_total =
  delivery.order_count +
  refund_after.order_count +
  waite_settle +
  settle.order_count +
  r_settle.order_count;
var deliver_p_count =
  delivery.p_count +
  refund_after.p_count +
  waite_settle_p_count +
  settle.p_count +
  r_settle.p_count;
var deliver_percent = (deliver_total / pay_count).toFixed(2);

var content =
  "|渠道|订单|付款|付款率|付款额|\
  前退|前退率|后退|后退率|\
  退款|退款率|发途|发途件|发途率|发途额|\
  备货|备货件|备货率|备货额|\
  总发|总发件|总发率|\
  待结算|待结件|待结算率|待结算额|\
  结算|结算件|结算率|结算额|\
  反结算|反结算件|反结算率|反结算额|平台服务费|\n" +
  "|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n";
content += `|总数| ${total_orders}|${pay_count}|${pay_percent}|${pay_amount}|\
${refund_before.order_count}|${refund_before.percent}|\
${refund_after.order_count}|${refund_after.percent}|\
${total_refund}|${total_refund_percent}|\
${delivery.order_count}|${delivery.p_count} |${delivery.percent} |${delivery.need_pay_mount} |\
${prepare.order_count}|${prepare.p_count} |${prepare.percent} |${prepare.need_pay_mount} |\
${deliver_total}|${deliver_p_count} |${deliver_percent} |\
${waite_settle}|${waite_settle_p_count} |${waite_settle_percent} |${waite_settle_mount} |\
${settle.order_count}|${settle.p_count} |${settle.percent} |${settle.need_pay_mount} |\
${r_settle.order_count}|${r_settle.p_count} |${r_settle.percent} |${r_settle.need_pay_mount} |\
${platform_service_amount}|\n`;

dashboard.setMarkdownOption(content);
