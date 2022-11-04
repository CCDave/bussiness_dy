const logic = load("logic.js");
informat.plugin = {
  api: [
    {
      id: "testApi",
      action: (ctx) => {
        console.log(ctx);
        return logic.init_refund_table_data();
      },
    },
  ],
  tableSource: [
    {
      module: "订单表-原始表",
      type: "postgresql",
      dbUrl: "jdbc:postgresql://121.41.19.35:5432/postgres",
      dbUser: "postgres",
      dbPassword: "SRwHwWnL24kAwsDs",
      tableName: "OrdersModel_orders",
      enableUpdate: true,
      enableDelete: true,
      enableInsert: true,
      autoIncrementFields: ["id"],
      fieldMapping: {
        id: "id",
        主订单编号: "parent_id",
        子订单编号: "order_id",
        商品ID: "p_id",
        商品数量: "p_count",
        商品名称: "name",
        商品规格: "p_specs",
        SKU拼接码: "sku_code",
        商品单价: "p_price",
        省: "province",
        订单应付金额: "payable",
        订单状态: "order_status",

        订单提交时间: "order_submit_time",
        订单提交日期: "order_submit_date",
        订单提交月份: "order_submit_month",
        发货时间: "express_delivery_time",
        发货日期: "express_delivery_date",
        几天发货: "express_delivery_days",

        售后类型: "post_sale_type",
        售后状态: "post_sale_status",
        售后申请时间: "post_sale_apply_time",
        售后申请日期: "post_sale_apply_date",
        几天退款: "refund_days",

        售后备注: "after_sale_remarks",
        仲裁状态: "arbitration_status",
        纠纷责任方: "responsible",
        商家备注: "shop_remarks",
        取消原因: "cancel_reason",
        售后原因: "post_sale_reason",
        售后原因标签: "post_sale_reason_tag",

        结算时间: "settle_time",
        结算日期: "settle_date",
        几天结算: "settle_days",
        结算金额: "settle_amount",
        收入合计: "total_income",
        平台服务费: "platform_service_amount",
        支出合计: "platform_service_amount",

        支付方式: "pay_way",
        手续费: "service_charge",
        订单阶段: "r_order_status",
        结算阶段: "r_order_settle_status",
        SKU编码: "s_sku_finish_code",
        供应商: "s_supplier",
      },
    },
    {
      module: "商品管理",
      type: "postgresql",
      dbUrl: "jdbc:postgresql://121.41.19.35:5432/postgres",
      dbUser: "postgres",
      dbPassword: "SRwHwWnL24kAwsDs",
      tableName: "OrdersModel_orders_link",
      enableUpdate: true,
      enableDelete: true,
      enableInsert: true,
      autoIncrementFields: ["id"],
      fieldMapping: {
        商品名称: "prod_name",
        关联订单: "order_list",
      },
    },
  ],
};
