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
}

const product_id = dashboard.getParameter("商品ID");
const full_sku_code = dashboard.getParameter("SKU");
const start_date = dashboard.getParameter("下单日期-开始");
const end_date = dashboard.getParameter("下单日期-结束");
const supply = dashboard.getParameter("供应商");
show_log([
  product_id == null ? 0 : product_id,
  full_sku_code == null ? 1 : full_sku_code,
  start_date == null ? 2 : start_date,
  end_date == null ? 3 : end_date,
  supply == null ? 4 : supply,
]);
