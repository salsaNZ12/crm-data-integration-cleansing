import pandas as pd
import time

print("[INFO] Starting CRM Administrative Data Pipeline...")
start_time = time.time()

# PHASE 1: DATA INGESTION & AUTOMATED MERGING
print("\n[PHASE 1] Loading and synchronizing CRM datasets...")
df_basic = pd.read_csv("customer_support_tickets.csv")
df_enhanced = pd.read_csv("enhanced_customer_support_data.csv")

# Synchronizing disconnected rows into a unified dataframe
df_master = pd.merge(df_basic, df_enhanced, how="inner")
print(f"[SUCCESS] Combined source records into {df_master.shape[0]} master rows.")


# PHASE 2: ADVANCED DATA HYGIENE & STANDARDIZATION
print("\n[PHASE 2] Executing text cleansing and normalization algorithms...")

# 1. Standardize Customer Names to Title Case
if 'Customer_Name' in df_master.columns:
    df_master['Customer_Name'] = df_master['Customer_Name'].astype(str).str.strip().str.title()

# 2. Unify Customer Emails to lowercase
if 'Customer_Email' in df_master.columns:
    df_master['Customer_Email'] = df_master['Customer_Email'].astype(str).str.strip().str.lower()

# 3. Handle Missing Administrative Values
if 'Priority_Level' in df_master.columns:
    df_master['Priority_Level'] = df_master['Priority_Level'].fillna("Medium")

print("[SUCCESS] Data hygiene and cleaning scripts completed.")


# PHASE 3: BULK DATA EXPORT FOR CORPORATE REPORTING
print("\n[PHASE 3] Compiling and exporting clean master file...")
output_filename = "cleaned_crm_master_database.csv"
df_master.to_csv(output_filename, index=False)

execution_time = round(time.time() - start_time, 2)
print(f"[STATUS] Pipeline successfully executed in {execution_time} seconds.")
print(f"[STATUS] Output saved to: '{output_filename}'\n")


# PHASE 4: FINAL AUDIT TRAIL VERIFICATION
print("=== FINAL PIPELINE AUDIT TRAIL ===")
columns_to_show = ['Ticket_ID', 'Customer_Name', 'Customer_Email', 'Issue_Category', 'Priority_Level']
print(df_master[columns_to_show].head())