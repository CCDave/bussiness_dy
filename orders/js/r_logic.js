const tool = load("tool.js");
const collect = load("collect.js");

(function logic() {
  function init_refund_table_data(params) {
    let product_id = params["product_id"];
    let full_sku_code = params["full_sku_code"];
    let start_date = params["start_date"];
    let end_date = params["end_date"];
    let supply = params["supply"];

    var table = new tool.table("订单表-原始表");
    table.init_table([
      "子订单编号",
      "商品单价",
      "商品数量",
      "结算金额",
      "订单应付金额",
      "平台服务费",
      "商品ID",
      "订单阶段",
      "结算阶段",
      "供应商",
      "订单提交日期",
      "结算日期",
      "几天发货",
      "几天退款",
      "几天结算",
      "SKU编码",
    ]);

    var headers = ["类型", "订单数", "付款数"];
    for (var i = 0; i < 20; i++) {
      headers.push(`${i}天`);
    }

    var index = [
      "退货",
      "退货总",
      "退货率",
      "退货率总",
      "发前数",
      "发前总",
      "发前率",
      "发前率总",
    ];
    var dash_board_refund = new tool.dashboard_tool(table, headers, index);
    var filter = dash_board_refund.init_order_filter(
      product_id,
      full_sku_code,
      start_date,
      end_date,
      supply
    );

    let query_set = {
      useFieldName: true,
      groupByFieldList: table.get_field_id_list(["几天退款", "订单阶段"]),
      aggregationQueryList: [
        {
          field: table.get_field_id("子订单编号"),
          func: "count",
          distinct: false,
        },
        { field: table.get_field_id("商品数量"), func: "sum", distinct: false },
      ],
    };

    if (filter.conditionList.length > 0) {
      query_set.filter = filter;
    }

    var resp = table.query(query_set);

    var data = resp.list;

    var c = collect(data);

    var total_orders_count = tool.array_sum_by_condition(
      c,
      null,
      "子订单编号_数量"
    );

    var no_pay_orders = tool.array_sum_by_condition(
      c,
      { 订单阶段: "未付款" },
      "子订单编号_数量"
    );

    var pay_orders_count = total_orders_count - no_pay_orders;
    var dash_data = new Array(dash_board_refund.headers.length); //.fill([]);
    var total_refund = 0;
    var total_refund_before = 0;
    for (var i = 0; i < dash_board_refund.headers.length; i++) {
      dash_data[i] = new Array(dash_board_refund.index);
      for (var j = 0; j < dash_board_refund.index.length; j++) {
        if (i == 0) {
          dash_data[i][j] = total_orders_count;
        } else if (i == 1) {
          dash_data[i][j] = pay_orders_count;
        } else {
          let index = i - 2;
          if (j == 0) {
            dash_data[i][j] = tool.array_sum_by_condition(
              c,
              { 几天退款: index },
              "子订单编号_数量"
            );
            total_refund += dash_data[i][j];
          } else if (j == 1) {
            dash_data[i][j] = total_refund;
          } else if (j == 2) {
            dash_data[i][j] = (
              (tool.array_sum_by_condition(
                c,
                { 几天退款: index },
                "子订单编号_数量"
              ) /
                pay_orders_count) *
              100
            ).toFixed(2);
          } else if (j == 3) {
            dash_data[i][j] = ((total_refund / pay_orders_count) * 100).toFixed(
              2
            );
          } else if (j == 4) {
            dash_data[i][j] = tool.array_sum_by_condition(
              c,
              { 几天退款: index, 订单阶段: "发货前退款" },
              "子订单编号_数量"
            );
            total_refund_before += dash_data[i][j];
          } else if (j == 5) {
            dash_data[i][j] = total_refund_before;
          } else if (j == 6) {
            dash_data[i][j] = (
              (tool.array_sum_by_condition(
                c,
                { 几天退款: index, 订单阶段: "发货前退款" },
                "子订单编号_数量"
              ) /
                pay_orders_count) *
              100
            ).toFixed(2);
          } else if (j == 7) {
            dash_data[i][j] = (
              (total_refund_before / pay_orders_count) *
              100
            ).toFixed(2);
          }
        }
      }
    }
    return dash_board_refund.convert_array_to_table_txt(dash_data);
  }
  return {
    init_refund_table_data: init_refund_table_data,
  };
})();
