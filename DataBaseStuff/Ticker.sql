-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/mccA5K
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Ticker" (
    "Volume" DECIMAL   NOT NULL,
    "Volume_Weighted_Average_Price" DECIMAL   NOT NULL,
    "Open_Price" DECIMAL   NOT NULL,
    "Closing_Price" DECIMAL   NOT NULL,
    "Day_Highest" DECIMAL   NOT NULL,
    "Day_Lowest" DECIMAL   NOT NULL,
    "Date" timestamp   NOT NULL,
    "Number_of_Transaction" int   NOT NULL
);

