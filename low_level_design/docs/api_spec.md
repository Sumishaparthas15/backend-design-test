# API Spec (REST)
Base URL: http://127.0.0.1:8000/api/v1/

## Authentication
- POST /api/token/  -> returns {access, refresh}
- Use header: Authorization: Bearer <access_token>


### 1. Submit Translation
POST
http://127.0.0.1:8000/api/v1/translate/

Headers:
  - Content-Type: application/json
  - Authorization: Bearer <token>

Body:
{
  "source_text": "Hello I am Sumisha PS from Kerala but currently I am in Bangalore",
  "source_lang": "en",
  "target_lang": "hi",
  "priority": "normal"
}
Responses:
201
Created
13 ms
502 B
1234567

    {
        "id": "64953890-da23-41da-a2a5-9b461fea5a9d",    
        "source_text": "Hello I am Sumisha PS from Kerala but currently I am in Bangalore",    
        "source_lang": "en",    
        "target_lang": "hi",    
        "priority": "normal"
    }



### 2. Get Status
GET
http://127.0.0.1:8000/api/v1/translate/64953890-da23-41da-a2a5-9b461fea5a9d/status/
Headers:
  - Authorization: Bearer <token>
Responses:
200
OK

{"id": "64953890-da23-41da-a2a5-9b461fea5a9d",    
"status": "completed",    "priority": "normal",    
"created_at": "2025-11-13T17:13:21.827306Z",    
"started_at": "2025-11-13T17:13:21.838375Z",   
 "completed_at": "2025-11-13T17:13:23.103021Z",    
 "word_count": 13}    



### 3. Get Result
 GET
http://127.0.0.1:8000/api/v1/translate/64953890-da23-41da-a2a5-9b461fea5a9d/result/
Headers:
  - Authorization: Bearer <token>
Responses:
200
OK

{    
    "id": "64953890-da23-41da-a2a5-9b461fea5a9d",   
     "status": "completed",    
     "translated_text": "हैलो मैं केरल की सुमिशा पीएस हूं लेकिन वर्तमान में मैं बैंगलोर में हूं",    
     "error_message": null
     }

### 4. Admin: List all jobs
Permission: admin only

GET
http://127.0.0.1:8000/api/v1/translate/all/

Headers:
  - Authorization: Bearer <token>
  
Response:
  200 OK: 
OK
6 ms
4.73 KB

    [
    {
        "id": "64953890-da23-41da-a2a5-9b461fea5a9d",
        "user": 2,
        "source_text": "Hello I am Sumisha PS from Kerala but currently I am in Bangalore",
        "translated_text": "हैलो मैं केरल की सुमिशा पीएस हूं लेकिन वर्तमान में मैं बैंगलोर में हूं",
        "source_lang": "en",
        "target_lang": "hi",
        "status": "completed",
        "priority": "normal",
        "word_count": 13,
        "error_message": null,
        "created_at": "2025-11-13T17:13:21.827306Z",
        "started_at": "2025-11-13T17:13:21.838375Z",
        "completed_at": "2025-11-13T17:13:23.103021Z"
    },
    {
        "id": "c7b42bdc-8b7d-41d4-a8f1-c333581958a4",
        "user": 2,
        "source_text": "Hello I am Sumisha PS from kerala but currently iam in banglore",
        "translated_text": "ഹലോ ഞാൻ കേരളത്തിൽ നിന്നുള്ള സുമിഷ പി .എസ്. എന്നാൽ നിലവിൽ ഞാൻ ബാംഗ്ലൂരിലാണ്",
        "source_lang": "en",
        "target_lang": "ml",
        "status": "completed",
        "priority": "normal",
        "word_count": 12,
        "error_message": null,
        "created_at": "2025-11-13T17:12:25.955360Z",
        "started_at": "2025-11-13T17:12:25.966680Z",
        "completed_at": "2025-11-13T17:12:26.975339Z"
    },
    {
        "id": "bf95edea-ee72-4b48-a360-83576defff74",
        "user": 2,
        "source_text": "Hello I am Sumisha PS from kerala but currently iam in banglore",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "mal",
        "status": "failed",
        "priority": "normal",
        "word_count": 12,
        "error_message": "Translation API returned empty text.",
        "created_at": "2025-11-13T17:11:22.803346Z",
        "started_at": "2025-11-13T17:11:22.845727Z",
        "completed_at": "2025-11-13T17:11:23.684304Z"
    },
    {
        "id": "21afa440-6f40-4451-9e47-913eee09f0e0",
        "user": 2,
        "source_text": "Hello I am Sumisha PS from kerala but currently iam in banglore",
        "translated_text": "Bonjour je suis Sumisha PS du kerala mais actuellement iam à banglore",
        "source_lang": "en",
        "target_lang": "fr",
        "status": "completed",
        "priority": "normal",
        "word_count": 12,
        "error_message": null,
        "created_at": "2025-11-13T17:09:05.592627Z",
        "started_at": "2025-11-13T17:09:05.674114Z",
        "completed_at": "2025-11-13T17:09:10.256760Z"
    },
    {
        "id": "9aa19202-48b6-4c16-bac7-11f96f5bddae",
        "user": 2,
        "source_text": "Hello iam sumisha ps from banglore",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "failed",
        "priority": "normal",
        "word_count": 6,
        "error_message": "'coroutine' object has no attribute 'text'",
        "created_at": "2025-11-13T17:01:56.670649Z",
        "started_at": "2025-11-13T17:01:56.730132Z",
        "completed_at": null
    },
    {
        "id": "b367697b-b9e8-4245-9638-8e25f424f365",
        "user": 2,
        "source_text": "Hello iam sumisha ps from banglore",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "pending",
        "priority": "normal",
        "word_count": 6,
        "error_message": null,
        "created_at": "2025-11-13T16:59:31.875958Z",
        "started_at": null,
        "completed_at": null
    },
    {
        "id": "c82e0077-b758-4d2c-b8a7-7a2cdbb77c78",
        "user": 2,
        "source_text": "Hello iam sumisha ps from kerala",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "failed",
        "priority": "high",
        "word_count": 6,
        "error_message": "'coroutine' object has no attribute 'text'",
        "created_at": "2025-11-13T16:57:30.834252Z",
        "started_at": "2025-11-13T16:57:30.896525Z",
        "completed_at": null
    },
    {
        "id": "01196741-327f-45bc-a807-7b8600eb6c5c",
        "user": 2,
        "source_text": "Hello iam sumisha ps from kerala",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "failed",
        "priority": "high",
        "word_count": 6,
        "error_message": "'coroutine' object has no attribute 'text'",
        "created_at": "2025-11-13T16:51:49.055803Z",
        "started_at": "2025-11-13T16:51:49.141341Z",
        "completed_at": null
    },
    {
        "id": "eb322074-34d9-41f8-bba9-6020acf71bfc",
        "user": 2,
        "source_text": "Hello world",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "completed",
        "priority": "normal",
        "word_count": 2,
        "error_message": null,
        "created_at": "2025-11-13T16:02:07.763700Z",
        "started_at": null,
        "completed_at": "2025-11-13T16:26:56.095515Z"
    },
    {
        "id": "511efe24-cdf7-49b6-bd06-e6b0e4e75c31",
        "user": 1,
        "source_text": null,
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "pending",
        "priority": "normal",
        "word_count": 0,
        "error_message": null,
        "created_at": "2025-11-13T11:59:45.116893Z",
        "started_at": null,
        "completed_at": null
    },
    {
        "id": "2a6296c1-27e8-4a61-b8e9-c0c539cab284",
        "user": 1,
        "source_text": "Hello world this is a translation job test",
        "translated_text": null,
        "source_lang": "en",
        "target_lang": "fr",
        "status": "pending",
        "priority": "high",
        "word_count": 8,
        "error_message": null,
        "created_at": "2025-11-13T11:54:17.004111Z",
        "started_at": null,
        "completed_at": null
    }
]