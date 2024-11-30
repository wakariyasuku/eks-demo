import streamlit as st
import pandas as pd

def main():
    st.title('表をmarkdown記法に変換するアプリ')

    # 行数と列数の指定
    num_rows = st.number_input('行数を入力してください', min_value=1, value=5, step=1)
    num_cols = st.number_input('列数を入力してください', min_value=1, value=3, step=1)

    # 空のDataFrameを作成
    df = pd.DataFrame('', index=range(num_rows), columns=[f'列{col+1}' for col in range(num_cols)])

    # ユーザーが入力できる表を表示
    st.write("各セルに入力してください:")
    edited_df = st.data_editor(df)

    # マークダウン形式に変換するボタン
    if st.button('Convert to code in markdown format'):
        markdown_code = generate_markdown(edited_df)
        st.markdown('**Markdown Format Code:**')
        st.code(markdown_code)

def generate_markdown(df):
    # DataFrameをマークダウン形式の文字列に変換
    return df.to_markdown(index=False)

if __name__ == '__main__':
    main()
