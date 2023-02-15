import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i + 1)
	time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
	right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は：', text
# 'コンディション：', condition

# st.write(option)

# if st.checkbox('Show Image'):
# 	img = Image.open('./data/IMG_9188.JPG')
# 	st.image(img, caption='My Profile', use_column_width=True)

# df = pd.DataFrame(
# 	np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
# 	columns=['lat', 'lon']
# )
# st.table(df.style.highlight_max(axis=0))
# st.bar_chart(df)
# st.map(df)
