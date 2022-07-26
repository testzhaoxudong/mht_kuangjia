from BSTestRunner import BSTestRunner
import unittest

import time

case_path='../test_case'
discover=unittest.defaultTestLoader.discover(case_path,pattern='test_*.py')
report_path='../reports'
now=time.strftime("%Y%m%d%H%M%S")
report_name=report_path+'/'+now+"test_report.html"

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title="mht test report",description="登录测试")
    runner.run(discover)