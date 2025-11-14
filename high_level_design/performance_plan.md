### Performance Requirements

How to make translations fast and handle large word doccuments efficiently.
    1. improve speed : group multiple translation requests together, process them in one opertaion instead of individually
    2: Break large doccuments into smaller chunks
    3: Keep GPU ready and share them efficiently among Celery workers.
    4: Store translations of frequently used phrases
    5: Use Celery to process translation jobs in the background.
    6: Load only necessary parts of the model.
    7: Combine chunks and  return final translation to user.
