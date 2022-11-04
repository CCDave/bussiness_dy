(function tool() {
  function array_sum_by_condition(c, conditions, sum_value) {
    return c.sum((product) => {
      var hit = true;
      if (conditions != null) {
        for (var key in conditions) {
          if (product[key] == undefined || product[key] != conditions[key]) {
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
  }

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
      this.field_list = field_list;

      for (let i = 0; i < field_name_list.length; i++) {
        var name = field_name_list[i];
        var field = this.get_field(field_list, name);
        if (name != null && field != null) {
          this.ids[name] = field.id;
          ret = true;
        }
      }
      console.log({
        table: this.table,
        table_id: this.table_id,
        ids: this.ids,
      });
      return ret;
    };

    this.get_field_id_list = function (name_list) {
      var ret = [];
      for (var i = 0; i < name_list.length; i++) {
        var field = this.get_field(name_list[i]);
        if (field) {
          ret.push(field.id);
        }
      }
      return ret;
    };

    this.get_field = function (name) {
      return this.field_list.find((f) => f.name == name);
    };

    this.get_field_id = function (name) {
      var field = this.field_list.find((f) => f.name == name);
      return field.id;
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
          fieldId: this.table.get_field_id("商品ID"),
          opt: "eq",
          value: product_id,
        });
      }
      if (full_sku_code != null) {
        filter.conditionList.push({
          fieldId: this.table.get_field_id("SKU编码"),
          opt: "contains",
          value: full_sku_code,
        });
      }

      if (start_date != null && end_date != null) {
        filter.conditionList.push({
          fieldId: this.table.get_field_id("订单提交日期"),
          opt: "ge",
          value: start_date,
        });
        filter.conditionList.push({
          fieldId: this.table.get_field_id("订单提交日期"),
          opt: "le",
          value: end_date,
        });
      } else if (
        (start_date != null && end_date == null) ||
        (start_date == null && end_date != null)
      ) {
        filter.conditionList.push({
          fieldId: this.table.get_field_id("订单提交日期"),
          opt: "eq",
          value: start_date == null ? end_date : start_date,
        });
      }
      if (supply != null) {
        filter.conditionList.push({
          fieldId: this.table.get_field_id("供应商"),
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
    this.convert_array_to_table_txt = function (data) {
      var content = "|";
      var split_str = "|";

      for (var i = 0; i < this.headers.length; i++) {
        content += `${this.headers[i]} |`;
        split_str += "-|";
      }
      content += "\n";
      content += split_str;
      content += "\n";
      for (var j = 0; j < this.index.length; j++) {
        content += `|${this.index[j]}|`;
        for (var i = 0; i < data.length; i++) {
          content += `${data[i][j]}|`;
        }
        content += "\n";
      }
      return content;
    };
  };
  return {
    dashboard_tool: dashboard_tool,
    table: table,
    DB_BASE: DB_BASE,
    array_sum_by_condition: array_sum_by_condition,
  };
})();
