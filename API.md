# API

## Summary

| Method | URL          | Input   | Output | Description        |
| ------ | ------------ | ------- | ------ | ------------------ |
| GET    | `/user`      | User    | Info   | Show an User Info  |
| POST   | `/user`      | User    |        | Sign Up            |
| POST   | `/qr`        | User ID | PNG    | Create QR Code     |
| POST   | `/gps`       | GPS     |        | GPS Device Decoder |
| GET    | `/translate` | Text    | Text   | Google Translate   |





```json
// GET /user request
{
    "event_name": "이벤트네임",
    "user_id" : "xxxxxxxx"
}
```

```json
// GET /user response
{
    "user_name": "사용자이름",
    "QR_code" : "img url링크"
    "item_list": [
    	{
			"gimbap": 1,
    		"NCE token": 0,
    		"rakuten credit": 0
    		// optional 정보. 추가내용에 따라 변동가능.
		}
    ]
}
```



```json
//POST /user request
{
    "event_name": "이벤트네임",
    "user_name": "xxx",
    "user_phone": "xxx"
}
```

```json
//POST /user response
{
    "status_code": "200"
    	// 200 or 400
}
```


```json
//POST /gps request
{
    "user_id": "XXXX",
    "longitude": "52.135236",
    "latitude": "23.22121424
}
```

```json
//POST /gps response
{
    'status_code':'404',
    'qr_image':'이밎URL' #QR코드 없을때,범위바깥일땐 빈칸.

```


-----


```json
 /translate request
{
    "text": "~~~~~~~~~~",
    "lang_code": "언어코드 us, kr같은거"
}
```


```json
/translate response
{
    "translate_text": "~~번역된 언어"
}

```


```json
/event request
{
	'event_name': "행사명"
}
```

```json
/event response
{
	'status_code':'200',
	'event_name': '행사명',
	'entry': '행사의 참가자들',
	'start_date': '시작일자"%Y,%m,%d,%H,%M,%S"',
	'end_date': '"%Y,%m,%d,%H,%M,%S"',
	'location': '위도 경도',
	'description': '행사설명'
}
```

