module.exports = {
	
	//获取日期
	getSysDate() {
	  const date = new Date();
	  var year = date.getFullYear();
	  var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date.getMonth() + 1;
	  var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
	  return `${year}-${month}-${day}`;
	},
	
	//数据分组
	arrayGroup(data, field) {
	  return data.reduce((res, item) => {
	    const groupKey = item[field];
	    if(!res[groupKey]) {
	      res[groupKey] = [];
	    }
			res[groupKey].push(item);
	    return res;
	  }, {});
	},
	
	//获取星期
	getWeekDay(date) {
	  const weekdays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
	  const weekday = new Date(date).getDay();
	  return weekdays[weekday];
	}
	
}
