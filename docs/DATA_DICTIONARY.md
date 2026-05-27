# Data Dictionary

## Tables & Fields

### Sales Data Table

| Field Name | Data Type | Description |
|---|---|---|
| transaction_id | Integer | Unique transaction identifier |
| date | Date | Date of transaction |
| region | String | Geographic region |
| product | String | Product sold |
| quantity | Integer | Units sold |
| revenue | Decimal | Total revenue from transaction |
| customer_id | Integer | Customer identifier |
| sales_person | String | Sales representative name |

### Regional Data Table

| Field Name | Data Type | Description |
|---|---|---|
| region_id | Integer | Unique region identifier |
| region_name | String | Name of the region |
| country | String | Country of the region |
| population | Integer | Population size |
| market_size | Decimal | Market size estimation |

## Data Quality Notes

- All monetary values in USD
- Date format: YYYY-MM-DD
- Missing values handled as per data cleaning protocol
