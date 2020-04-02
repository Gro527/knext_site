# 知识抽取工具api文档

## 用户管理类
#### 1. 用户注册
		uri: /api/v1/signup
		method: POST
		headers: {
			"Content-Type": "application/json"
		}
		payload: {
			"username": string,
			"password": string
		}
		response: {
			"status": int, 		//正常情况为0，请求错误时为-1
			"message": string, 		//错误信息，正常情况下为"ok"
			"data": {}
		}
#### 2. 用户登录
		uri: /api/v1/login
		method: POST
		headers: {
			"Content-Type": "application/json"
		}
		payload: {
			"username": string,
			"password": string
		}
		response: {
			"status": int,
			"message": string,
			"data": {}
		}
#### 3. 密码修改
		//login required
		uri: /api/v1/pw_change
		method: POST
		headers: {
			"Content-Type": "application/json"
		}
		payload: {
			"password": string,
			"new_password": string
		}
		response: {
			"status": int,
			"message": string,
			"data": {}
		}
#### 4. token申请
		//login required
		//获取token，用于第三方接入知识抽取接口
		uri: /api/v1/token
		method: GET
		response: {
			"status": int,
			"message": string,
			"data": {
				"token": string,
			}
		}

## 知识抽取功能
#### 1. 知识抽取接口
		//login required
		uri: /api/v1/extract
		method: POST
		headers: {
			"Content-Type": "application/json"
		}
		payload: {
			"text": string, 	//需要进行抽取的文本
			"model_type": string, 		//模型类型
		}
		response: {
			"status": int,
			"message": string,
			"data": {
				"text": string, 	//原文
				"kn": [{
						"subject": string, 	//知识主体
						"relation": string, 	//关系
						"object": string, 	//知识客体
					},
					...
				]，
				"server_info": string 	//服务方信息
			}
		}
#### 2. 知识标注接口
		//login required
		uri: /api/v1/mark
		method: PUT
		headers: {
			"Content-Type": "application/json"
		}
		payload: {
			"text": string, 	//需要进行标注的文本
			"model_type": string,
			"kn": [{
					"subject": string, 	//知识主体
					"relation": string, 	//关系
					"object": string, 	//知识客体
				},
				...
			]
		}
		response: {
			"status": int,
			"message": string,
			"data": {}
			}
		}
#### 3. badcase标注接口
		//login required
		uri: /api/v1/badcase
		method: PUT
		headers: {
			"Content-Type": "application/json"
		}
		payload: {
			"text": string, 	//需要进行badcase标注的文本
			"model_type": string,
			"kn": [{
					"subject": string, 	//知识主体
					"relation": string, 	//关系
					"object": string, 	//知识客体
				},
				...
			]
		}
		response: {
			"status": int,
			"message": string,
			"data": {}
			}
		}
