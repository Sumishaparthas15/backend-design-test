### Monitoring and Costs Plan

Detects problems early before users complain.

# 1.Keeping Track of System Health
step1 :watching your system to make sure it’s working properly
step2 :collect metrics from your servers and workers
step3 :Set up notifications if something goes wrong

# 2.Cost Estimation For Knowing How Much It Costs
Helps plan budgets and avoid overspending
step1: calculate GPU cost per hour
        1 GPU =100/hr
        2 GPU =2*2*100/hr =400
step2: calculate CPU cost for API servers
        2 CPU = 1/hr
        24 hrs = 1*2*24        
step3: storage cost
step4: tips:Stop idle workers  during low traffic to save money.       


    1.Metrics collected from API and workers.
    2.Dashboards show system health.
    3.Alerts trigger when something goes wrong.
    4.Helps track usage and estimate costs.


Users -> API -> Celery queue  ->  GPU Workers  -> Database-> Alerts -> Action
