Attribute VB_Name = "StockTicker"
' Reads the ticker column and to column J and removes duplicates from column J
Sub get_unique()
    ' Developer note: the data should be sorted before removing duplicates
    ' It is assumed this data is sorted
    Dim row As Long
    ' Finds the last cell in the column
    row = Cells(Rows.Count, "A").End(xlDown).row
    ' Copy column A to column J
    ActiveSheet.Range("A1:A" & row).Copy ActiveSheet.Range("J1")
    ' Remove duplicates from column J
    ActiveSheet.Range("J1:J" & Cells(Rows.Count, "J").End(xlUp).row).RemoveDuplicates Columns:=1, Header:=xlNo
    ' Add Ticker column header back
    ' It is overwritten by A1
    ' Starting at A2 was not good because there were two AABs
    ' According to documentation on StackOverFlow a header column is needed to remove all duplicates
    Cells(1, 10).Value = "Ticker"
End Sub
