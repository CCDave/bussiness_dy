const collect = load("collect.js");
(function tool() {
  const tool = function () {
    this.array_sum_by_condition = function (collect, conditions, sum_value) {
      return collect.sum((product) => {
        var hit = true;
        if (conditions && conditions.length > 0) {
          for (var key in conditions) {
            if (product[key] != conditions[key]) {
              hit = false;
              break;
            }
          }
        }
        if (hit) {
          return product[sum_value] ? product[sum_value] : 0;
        } else {
          return 0;
        }
      });
    };
  };

  const DB_BASE = function () {
    this.db_url = "jdbc:postgresql://121.41.19.35:5432/postgres";
    this.db_user = "postgres";
    this.db_password = "SRwHwWnL24kAwsDs";
    this.db_class_name = "org.postgresql.Driver";
    this.db_query = function (sql, params) {
      let data = {
        dburl: this.db_url,
        dbuser: this.db_user,
        dbpassword: this.db_password,
        driverClassName: this.db_class_name,
        sql: sql,
      };
      if (params !== null) {
        data.parameters = params;
      }
      return informat.jdbc.queryList(data);
    };
    this.db_update = function (sql, params) {
      let data = {
        dburl: this.db_url,
        dbuser: this.db_user,
        dbpassword: this.db_password,
        driverClassName: this.db_class_name,
        sql: sql,
      };
      if (params !== null) {
        data.parameters = params;
      }
      return informat.jdbc.executeUpdate(data);
    };
  };

  const table = function (name) {
    this.name = name;
    this.table = null;
    this.field_list = null;
    this.field_name_list = null;
    this.ids = {};
    this.table_id = null;

    this.init_table = function (field_name_list) {
      var ret = false;
      var table = informat.table.getTable(this.name);
      this.table = table;
      this.table_id = table.id;
      var field_list = informat.table.getFieldList(table.id);
      for (let i = 0; i < field_name_list.length; i++) {
        var name = field_name_list[i];
        var field_id = this.get_field(field_list, name);
        if (name != null && field_id != null) {
          this.ids[name] = field_id;
          ret = true;
        }
      }
      return ret;
    };
    this.get_field_list = function (name_list) {
      var ret = [];
      for (var i = 0; i < name_list; i++) {
        var field = this.get_field(this.field_list, name_list[i]);
        if (field) {
          ret.push(field);
        }
      }
    };
    this.get_field = function (field_list, name) {
      return field_list.find((f) => f.name == name);
    };

    this.insert = function (bean) {
      bean = informat.table.convert(this.field_list, bean);
      return informat.table.insert(this.table_id, bean);
    };

    this.update = function (bean) {
      bean = informat.table.convert(this.field_list, bean);
      return informat.table.update(this.table_id, bean);
    };

    this.query = function (query_set) {
      return informat.table.query(this.table_id, query_set);
    };
  };
  const dashboard_tool = function (table, headers, index) {
    this.table = table;
    this.headers = headers;
    this.index = index;
    this.init_order_filter = function (
      product_id,
      full_sku_code,
      start_date,
      end_date,
      supply
    ) {
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
      return filter;
    };
    this.dashboard_log = function (params) {
      var content =
        "| 参数                    | 类型   | 必填 | 备注           | \n" +
        "| ----------------------- | ------ | ---- | -------------- |\n";

      for (let i = 0; i < params.length; i++) {
        content += `| ${params[i]}          | String | 是   | 数据表ID       |\n`;
      }
      content += "|content                  | String | 是   | 富文本原始内容 |";
      return `参数：${JSON.stringify(params)}` + "<br>\n\n" + content;
    };
    this.convert_array_to_table_txt = function (data) {};
  };
  return {
    dashboard_tool: dashboard_tool,
    table: table,
    DB_BASE: DB_BASE,
    tool: tool,
  };
})();