 ### System Architecture:

 when a user ask transtalion:

 step1  : The user types text in  your web app
            [eg:a user wants to translate "Hello" from english to Hindi]

 step2  : The request arrive at Django Rest API
            [The API does main 2 thing:
                authentication,validation (make sure that text is exists,the source language and target language are correct)]  
            If something is wrong, the API immediately sends an error back.  

 step 3 : Celery picks the task from the queue.celery is system that lets you can tasks in the background,outside the main web request     

 step4  : GPU worker processes the translation, a seperate  background process picks up the jobs from the queue
          if the transaltion model uses GPU and that model takes the input text and generate the transaltion 
          [eg: "Hello" -> "हेलो"]    

 step5  : The translated text is saved in tht database
                Meta:
                   UserId,JobId,Timestamp, Status                      

 step6  : user can check the status and result ,the API directly returns the translated text



 Status tracking:

    pending    -> request added to queue
    processing -> worker is translating
    completed  -> translation ready
    error      -> something went wrong




                                                 User
                                                   ↓
                                         API (auth & validation)
                                                   ↓
                                             Celery queue
                                                   ↓
                                      GPU Worker(Translated Model)
                                                   ↓
                                                Database
                                                   ↓
                                                  API
                                                   ↓
                                                  User 

