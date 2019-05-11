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
//POST /qr request
{
    "event_name": "이벤트네임",
    "user_id": "xxxxxxx"
    	// (이름+전화번호)의 hash값
}
```

```json
//POST /qr response
{
    "qr_image": ".png파일"
     	//"https://~~~.png"
}
```

```json
//POST /gps request
{
    "longitude": "52.135236",
    "latitude": "23.22121424
}
```

```json
//POST /gps response
{
    "status": 200
}
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