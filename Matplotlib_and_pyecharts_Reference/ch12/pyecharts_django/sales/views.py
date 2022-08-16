import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts import options as opts
from pyecharts.charts import Bar, Page
from impala.dbapi import connect

#连接Hadoop数据库
v1 = []
v2 = []
v3 = []
conn = connect(host='192.168.1.7', port=10000, database='sales',auth_mechanism='NOSASL',user='root')
cursor = conn.cursor()

#读取Hadoop表数据
sql_num = "SELECT province,count(distinct order_id),count(distinct cust_id) FROM orders WHERE dt=2019 and return=0 GROUP BY province"
cursor.execute(sql_num)
sh = cursor.fetchall()
for s in sh:
    v1.append(s[0])
    v2.append(s[1])
    v3.append(s[2]) 

# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


#画直方图
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(v1)
        .add_yaxis("有效订单数", v2)
        .add_yaxis("有效客户数", v3, is_selected=True)        #is_selected默认是False，即不选中
        .set_global_opts(
            title_opts=opts.TitleOpts(title="有效订单与有效客户分析", subtitle="2019年企业经营状况分析"),
            toolbox_opts=opts.ToolboxOpts(),
			datazoom_opts=opts.DataZoomOpts(),
            legend_opts=opts.LegendOpts(is_show=True))
		.dump_options()
    )
    return c
	
class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())