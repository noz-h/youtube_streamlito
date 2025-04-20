import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit・超入門') # タイトルを入れる場合はst.title('')

st.write('プログレスバーの表示') # 何か文章を書くときはst.write('')

st.write('Start!!')

latest_iteration = st.empty()
bar = st.progress(0) # プログレスバーを表示する場合はst.progress(0)を使う。()の中はint型かfloat型の数字を入れる。

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i +1)
    time.sleep(0.1) # 0.1秒待つ。この場合、0.1秒ごとにプログレスバーが進む。

left_column, right_column = st.columns(2) # 2つのカラムを作る場合はst.columns(2)を使う。
button = left_column.button('右カラムに文字を表示') # 左カラムにボタンを作る場合はst.button('')を使う。
if button: # buttonが押されたら右カラムに文字を表示する。
    right_column.write('ここは右カラム') # 右カラムに文字を表示する場合はst.write('')を使う。

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く') # 展開する場合はst.expander('')を使う。


condition = st.slider('あなたの今の調子は？', 0, 100,50)
text = st.text_input('あなたの趣味を教えてください。')

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100,50) # スライダーを表示する場合はst.slider('')を使う。
# # st.slider('あなたの今の調子は？', 0, 100,50)は、あなたの今の調子は？というスライダーを表示する。0から100までのスライダーが表示され、初期値は50。
# text = st.sidebar.text_input('あなたの趣味を教えてください。') # テキストボックスを表示する場合はst.text_input('')を使う。
# st.sidebar.○○は、○○をサイドバーに表示することを意味する。


st.write('コンディション：', condition) # st.write('コンディション：', condition)は、コンディション：（スライダーで選んだ数字）と表示される。
st.write('あなたの趣味：', text) # st.write('あなたの趣味は、', text, 'です。')は、あなたの趣味は、（テキストボックスで入力した趣味）です。という風に表示される。   

# セレクトボックスを表示する場合はst.selectbox('')を使う。
option = st.selectbox( # セレクトボックスをoptionに格納する。
    'あなたが好きな数字を教えてください。',
    list(range(1, 11)), # list(range(1, 11))は1から10までの数字をリストにする。
)

st.write('あなたの好きな数字は、', option, 'です。') # st.write('あなたの好きな数字は、', option, 'です。')は、あなたの好きな数字は、1（セレクトボックスで選んだ数字）です。という風に表示される。

if st.checkbox('Show Image'): # チェックボックスを表示する場合はst.checkbox('')　チェックボックスにチェックが入っていたらTrue、入っていなかったらFalseが返ってくる。
    img = Image.open('SH380122.JPG')
    st.image(img, caption = 'cat', use_container_width = True) # 画像を表示する場合はst.image(img, caption = 'cat', use_container_width = True)を使う。

# st.image(img, caption = 'cat', use_container_width = True)の引数は以下の通り
# img: 画像のパスを指定する。caption: 画像のキャプションを指定する。use_container_width: Trueにするとカラム幅（実際のレイアウトの横幅）に合わせて画像を表示する。


df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [33.59, 130.40],
    columns = ['lat', 'lon']
)
st.map(df) # マッピングするときはst.map(df)を使う
# マッピング↑

# DataFrameを表示する場合はst.write(df)
# st.dataframe(df.style.highlight_max(axis=0)) # 最大値を強調表示する。axis=0は列方向に最大値を強調表示することを意味する。
# 表示する場合はst.dataframe(df)でもよい。st.dataframe(df)だと引数を指定することができる。特にwidthとheightなど
# スタティックな（静的な）表を表示する場合はst.table(df)を使う。st.table(df)は引数を指定することができない。ただの表を表示させたいときに使う。

# 折れ線グラフを表示させたいときはst.line_chart()を使う
# st.area_chart(df), st.bar_chart(df)など



# マークダウンを使うと見出しやリストを作成することができる。

# """
# # 章
# ## 節
# ### 項

# # Pythonのコードを書きますよ、という意味での書き方。
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """