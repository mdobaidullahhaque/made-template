#!/usr/bin/env python
# coding: utf-8

import os
import sqlite3
import pandas as pd
import subprocess


# Define paths and constants
DATA_DIR = "../data"
LIFE_EXP_CSV = os.path.join(DATA_DIR, "life_expectancy_cleaned.csv")
SOCIO_ECON_CSV = os.path.join(DATA_DIR, "socio_economic_cleaned.csv")
SQLITE_DB = os.path.join(DATA_DIR, "life_socio_economic_data.db")
PIPELINE_SCRIPT = "pipeline.py"


def test_pipeline_execution():
    
    #Test if the pipeline script executes successfully.
    
    print("Testing pipeline execution...")
    result = subprocess.run(["python", PIPELINE_SCRIPT], capture_output=True, text=True)
    assert result.returncode == 0, f"Pipeline script failed: {result.stderr}"
    print("Pipeline executed successfully.")


def test_life_exp_csv_exists():
    
    #Test if the Life Expectancy cleaned CSV file is created.
    
    print("Testing if Life Expectancy cleaned CSV exists...")
    assert os.path.exists(LIFE_EXP_CSV), f"Life Expectancy cleaned CSV file not found: {LIFE_EXP_CSV}"
    print("Life Expectancy cleaned CSV exists.")


def test_socio_econ_csv_exists():
    
    #Test if the Socio-Economic cleaned CSV file is created.
    
    print("Testing if Socio-Economic cleaned CSV exists...")
    assert os.path.exists(SOCIO_ECON_CSV), f"Socio-Economic cleaned CSV file not found: {SOCIO_ECON_CSV}"
    print("Socio-Economic cleaned CSV exists.")


def test_life_exp_csv_content():
    
    #Test the content of the Life Expectancy cleaned CSV file.
   
    print("Testing Life Expectancy cleaned CSV content.")
    df = pd.read_csv(LIFE_EXP_CSV)
    assert not df.empty, "Life Expectancy cleaned CSV file is empty."
    assert "Country Name" in df.columns, "Expected column 'Country Name' not found in Life Expectancy CSV."
    assert "Year" in df.columns, "Expected column 'Year' not found in Life Expectancy CSV."
    print("Life Expectancy cleaned CSV content is valid.")


def test_socio_econ_csv_content():
    
    #Test the content of the Socio-Economic cleaned CSV file.
    
    print("Testing Socio-Economic cleaned CSV content.")
    df = pd.read_csv(SOCIO_ECON_CSV)
    assert not df.empty, "Socio-Economic cleaned CSV file is empty."
    assert "Country Name" in df.columns, "Expected column 'Country Name' not found in Socio-Economic CSV."
    assert "Year" in df.columns, "Expected column 'Year' not found in Socio-Economic CSV."
    print("Socio-Economic cleaned CSV content is valid.")


def test_sqlite_db_exists():
    
    #Test if the SQLite database file is created.
    
    print("Testing if SQLite database exists...")
    assert os.path.exists(SQLITE_DB), f"SQLite database not found: {SQLITE_DB}"
    print("SQLite database exists.")


def test_sqlite_tables():
    
    #Test if the expected tables exist in the SQLite database.
    
    print("Testing SQLite database tables.")
    with sqlite3.connect(SQLITE_DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        assert "life_expectancy_data" in tables, "Table 'life_expectancy_data' not found in SQLite database."
        assert "socio_economic_data" in tables, "Table 'socio_economic_data' not found in SQLite database."
        print("Expected tables found in SQLite database.")


def test_sqlite_table_content():
    
    #Test the content of the tables in the SQLite database.
    
    print("Testing SQLite database table content...")
    with sqlite3.connect(SQLITE_DB) as conn:
        life_exp_df = pd.read_sql("SELECT * FROM life_expectancy_data;", conn)
        socio_econ_df = pd.read_sql("SELECT * FROM socio_economic_data;", conn)
        assert not life_exp_df.empty, "Table 'life_expectancy_data' in SQLite database is empty."
        assert not socio_econ_df.empty, "Table 'socio_economic_data' in SQLite database is empty."
        print("SQLite database tables contain valid data.")


if __name__ == "__main__":
    # Run all tests accordingly
    test_pipeline_execution()
    test_life_exp_csv_exists()
    test_socio_econ_csv_exists()
    test_life_exp_csv_content()
    test_socio_econ_csv_content()
    test_sqlite_db_exists()
    test_sqlite_tables()
    test_sqlite_table_content()

    print("All tests passed successfully.")





