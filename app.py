import streamlit as st
import boto3
import pandas as pd
import s3fs
import pyarrow.parquet as pq
import pyarrow as pa

# ---------------- CATEGORY MAP ----------------
CATEGORY_MAP = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    19: "Travel & Events",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "Howto & Style",
    27: "Education",
    28: "Science & Technology",
    29: "Nonprofits & Activism",
}

# ---------------- AWS SESSION ----------------
session = boto3.session.Session(
    aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
    region_name=st.secrets["AWS_DEFAULT_REGION"],
)

s3 = session.client("s3")
fs = s3fs.S3FileSystem(
    key=st.secrets["AWS_ACCESS_KEY_ID"],
    secret=st.secrets["AWS_SECRET_ACCESS_KEY"],
)

BUCKET = "de-on-youtube-analytics-ustateseast1-dev"
PREFIX = "final_analytics/"

# ---------------- DATA LOADER ----------------
@st.cache_data
def load_data():
    response = s3.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX)

    parquet_files = [
        f"s3://{BUCKET}/{item['Key']}"
        for item in response.get("Contents", [])
        if item["Key"].endswith(".parquet")
    ]

    tables = [pq.read_table(path, filesystem=fs) for path in parquet_files]
    full_table = pa.concat_tables(tables, promote=True)
    df = full_table.to_pandas()

    df["category_name"] = df["category_id"].map(CATEGORY_MAP)

    return df


# ---------------- MAIN HOME ----------------
st.set_page_config(
    page_title="YouTube Analytics Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("📊 YouTube Analytics Dashboard")
st.write("Navigate using the sidebar to explore insights.")

df = load_data()

st.subheader("Sample Dataset")
st.dataframe(df.head())
