import streamlit as st
import plotly.express as px

from finance import get_stock_data
from news import get_news
from sentiment import analyze_sentiment


st.set_page_config(
    page_title="AlphaMind AI",
    layout="wide"
)


st.title("🧠 AlphaMind AI")
st.subheader("Financial Market Intelligence Platform")
st.caption(
    "Disclaimer: AlphaMind AI provides AI-generated market insights "
    "for educational purposes only and does not provide financial advice."
)

companies = {
    "Apple 🍎": "AAPL",
    "Tesla 🚗": "TSLA",
    "Nvidia ⚡": "NVDA",
    "Microsoft 💻": "MSFT",
    "Google 🔍": "GOOGL",
    "Amazon 📦": "AMZN"
}


tabs = st.tabs(list(companies.keys()))


for tab, company in zip(tabs, companies):

    with tab:

        ticker = companies[company]

        st.header(f"{company} Market Intelligence")
        st.write(f"Ticker: **{ticker}**")


        if st.button(
            f"Analyze {ticker}",
            key=ticker
        ):

            with st.spinner("Analyzing market..."):


                try:

                    stock = get_stock_data(ticker)


                    st.header("📈 Market Data")


                    col1, col2, col3 = st.columns(3)


                    col1.metric(
                        "Current Price",
                        stock["price"]
                    )


                    col2.metric(
                        "Market Cap",
                        stock["market_cap"]
                    )


                    col3.metric(
                        "P/E Ratio",
                        stock["pe_ratio"]
                    )



                    history = stock["history"]


                    st.subheader("Price Movement")


                    fig = px.line(
                        history,
                        x=history.index,
                        y="Close",
                        title=f"{ticker} Stock Trend"
                    )


                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )



                    st.header("📰 News Intelligence")


                    news = get_news(ticker)


                    sentiments = analyze_sentiment(news)


                    positive = 0
                    negative = 0



                    for item in sentiments:


                        st.write(
                            "###",
                            item["article"]
                        )


                        st.write(
                            "Sentiment:",
                            item["sentiment"]
                        )


                        st.write(
                            "Confidence:",
                            item["confidence"],
                            "%"
                        )


                        if item["sentiment"] == "positive":
                            positive += 1


                        elif item["sentiment"] == "negative":
                            negative += 1



                    st.header("🤖 AI Market Summary")


                    if positive > negative:

                        st.success(
                            f"{ticker} shows positive market sentiment based on recent financial news."
                        )


                    elif negative > positive:

                        st.error(
                            f"{ticker} shows negative market sentiment based on recent financial news."
                        )


                    else:

                        st.warning(
                            f"{ticker} market sentiment is neutral."
                        )



                except Exception as e:

                    st.error(
                        "Unable to analyze this company right now."
                    )

                    st.write(e)