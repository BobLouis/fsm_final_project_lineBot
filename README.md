# Healthy Bear

## 構想
現在的人生活越來越忙碌，常常忘記運動 喝水 閱讀健康資訊 以及最重要的吃得健康吃得美味，因此我想要做一個healthy bear 來關心我們的健康狀況，帶我們吃得健康吃得開心，想要一直把這個linebot用在我們以後的生活中，而不是只有拿來交作業。

## 功能
根據提示可以進入不同的state 總共有5個功能，分別是餐食建議 計算BMI 計算喝水量 運動影片 以及最新新聞及健康資訊，每一個功能都會因應使用者的不同需求以及健康資訊而有不同的回覆




## 引用library
- Beautifulsoup4
    - 爬取新聞及健康資訊

## 使用教學
1. install `pipenv`
```shell
pip3 install pipenv
```
2. install 所需套件
```shell
pipenv install --three
// 若遇到pygraphviz安裝失敗，則嘗試下面這行
sudo apt-get install graphviz graphviz-dev
```
3. 從`.env.sample`產生出一個`.env`，並填入以下四個資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
4. install `ngrok`

```shell
sudo snap install ngrok
```
5. run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
6. execute app.py
```shell
python3 app.py
```

## 使用說明
- 基本操作
    輸入任意字 系統會回覆提示字元 照著提示字元即可進入進入相對應state
	`dine` -> 進入美食推薦
	`BMI` -> 測量BMI
	`water` -> 計算你一天所需要喝的水
	`sport` -> 根據你輸入的時間與強度給出事的影片
	`news` -> 用爬蟲給最新的新聞與健康資訊

## 使用示範
### 進入畫面
![](https://i.imgur.com/a77N0pw.png)

### 吃什麼
![](https://i.imgur.com/tidQM6o.png)
![](https://i.imgur.com/WDzeEzh.png)
![](https://i.imgur.com/LCb3yJB.png)
![](https://i.imgur.com/ycGBs2u.png)
![](https://i.imgur.com/xJx71Ei.png)
### 測量BMI
![](https://i.imgur.com/KG7UmYk.png)
![](https://i.imgur.com/48872CK.png)
![](https://i.imgur.com/qjc5P7Y.png)

### 喝水去
![](https://i.imgur.com/dSr3vJz.png)
![](https://i.imgur.com/KPCfMrp.png)
![](https://i.imgur.com/jDg5WhF.png)
### 運動去
![](https://i.imgur.com/cve394G.png)
![](https://i.imgur.com/srWrJS0.png)
![](https://i.imgur.com/astybQa.png)
![](https://i.imgur.com/9xwFmqU.png)
![](https://i.imgur.com/mu7H7N6.png)
![](https://i.imgur.com/kpbsSOE.png)

### 看新聞
![](https://i.imgur.com/C5XzZQG.png)
![](https://i.imgur.com/Q8JOqGc.png)
![](https://i.imgur.com/ZBYBWNO.png)




## Deploy in Heroku
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
    heroku config:set APP_KEY=your_olami_APP_KEY
    heroku config:set APP_SECRET=your_olami_APP_SECRET
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

