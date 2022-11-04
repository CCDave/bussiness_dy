function show_log(params) {
  var content =
    "| 参数                    | 类型   | 必填 | 备注           | \n" +
    "| ----------------------- | ------ | ---- | -------------- |\n";

  for (let i = 0; i < params.length; i++) {
    content += `| ${params[i]}          | String | 是   | 数据表ID       |\n`;
  }
  content += "|content                  | String | 是   | 富文本原始内容 |";
  dashboard.setMarkdownOption(
    `参数：${JSON.stringify(params)}` + "<br>\n\n" + content
  );
}

var qt_tool = {
  sumByCondtions: function sumByCondtion(c, con, sum) {
    return collect.sum((product) => {
      product[c_key] == c_value ? product[value] : 0;
    });
  },
};
