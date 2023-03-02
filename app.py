import streamlit as st
import random

def tengacha():
	n = random.randint(1, 1000)
	if n <= 6:
		m = random.randint(1, 2)
		if m == 1:
			st.text("レア度★★★★★の神里綾華を引きました！")
		else:
			p = random.randint(1, 5)
			if p == 1:
				st.text("レア度★★★★★のジンを引きました！")
			elif p == 2:
				st.text("レア度★★★★★の刻晴(こくせい)を引きました！")
			elif p == 3:
				st.text("レア度★★★★★のティナリを引きました！")
			elif p == 4:
				st.text("レア度★★★★★の七七(なな)を引きました！")
			else:
				st.text("レア度★★★★★のモナを引きました！")
	else:
		a = random.randint(1, 2)
		if a == 1:
			m = random.randint(1, 3)
			if m == 1:
				st.text("レア度★★★★の早柚(さゆ)を引きました！")
			elif m == 2:
				st.text("レア度★★★★のロサリアを引きました！")
			elif m == 3:
				st.text("レア度★★★★のレザーを引きました！")
		else:
			st.text("レア度★★★★のキャラもしくは武器を引きました！")

def gacha():
	n = random.randint(1, 1000)
	if n <= 6:
		m = random.randint(1, 2)
		if m == 1:
			st.text("レア度★★★★★の神里綾華を引きました！")
		else:
			p = random.randint(1, 5)
			if p == 1:
				st.text("レア度★★★★★のジンを引きました！")
			elif p == 2:
				st.text("レア度★★★★★の刻晴(こくせい)を引きました！")
			elif p == 3:
				st.text("レア度★★★★★のティナリを引きました！")
			elif p == 4:
				st.text("レア度★★★★★の七七(なな)を引きました！")
			else:
				st.text("レア度★★★★★のモナを引きました！")
	elif n <= 57:
		a = random.randint(1, 2)
		if a == 1:
			m = random.randint(1, 3)
			if m == 1:
				st.text("レア度★★★★の早柚(さゆ)を引きました！")
			elif m == 2:
				st.text("レア度★★★★のロサリアを引きました！")
			elif m == 3:
				st.text("レア度★★★★のレザーを引きました！")
		else:
			st.text("レア度★★★★のキャラもしくは武器を引きました！")
	else:
		st.text("レア度★★★の武器を引きました")

st.title("原神ガチャシミュレーター")
st.caption("原神の神里綾華ガチャを引くアプリです。")

#フォームの形成
with st.form(key="profile_form"):
	#ボタン
	gacha_btn = st.form_submit_button("ガチャを引く")
	tengacha_btn = st.form_submit_button("10連ガチャを引く")
	
	if gacha_btn == True:
		gacha()

	if tengacha_btn == True:
		for i in range(10):
			if i != 9:
				gacha()
			else:
				tengacha()