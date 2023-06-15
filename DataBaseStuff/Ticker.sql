-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/mccA5K
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Ticker" (
    "Volume" double   NOT NULL,
    "Volume_Weighted_Average_Price" double   NOT NULL,
    "Open_Price" double   NOT NULL,
    "Closing_Price" double   NOT NULL,
    "Day_Highest" double   NOT NULL,
    "Day_Lowest" double   NOT NULL,
    "Date" timestamp   NOT NULL,
    "Number_of_Transaction" int   NOT NULL
);

