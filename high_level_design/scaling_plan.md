### Scalability

when more users start using your translation service, the system need to handle extra load without slow and crashing 
How the system handles more users : horizontal and vertical.

# 1. Horizondal Scaling
    Add more machines to share the load
        1: Multiple API servers : a load balancer decides which server handles each request , if one server is busy the request goes to another server
        2: Multiple Celery Workers : instead of one worker picking transaltion jobs, you can run many workers in parallel,
        each workers can handle a transaltion job independally 
        3: Redis : If many jobs waiting use multiple Redis servers to share the load.


# 2. Vertical Scaling
    Instead of adding more machines,upgrade the existing machine
        1: API requests and background tasks that are CPU heavy will run faster.
        2: instead of Google Translate, a bigger GPU can handle more complex translations quickly.
        3: database grows with more translations bigger RAM prevents slowdowns.

# 3. idle periods to reduce costs

        1: During low traffic, reduce the number of celery workers
        2: If you use cloud GPUs, stop them when not in use.
        
# 4. translation requests
    Users can submit many large texts at the same time.
        1: without scaling : API may slow down or return errors ,Celery queue may get too long.
        2: With proper scaling: Many users are handled smoothly,translation jobs are processed quickly and reliably.


