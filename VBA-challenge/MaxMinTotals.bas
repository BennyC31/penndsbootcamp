Attribute VB_Name = "MaxMinTotals"
' Bonus module
' Calculates the highlights from the stocks
Sub callAll()
    ' Convenience method to call Max, Min, and Max Stock Volume methods
    Call findMaxIncrease
    Call findMindecrease
    Call findMaxStockVolume
End Sub
Sub findMaxIncrease()
    Dim lastrow As Variant
    Dim rng As Range
    Dim pct_max As Variant
    Dim cell_loc As String
    Dim c As Range
    Dim ticker_Addr As String
    Dim pct As Variant
    
    With ActiveSheet
        ' Finds the last cell in the column
        lastrow = .Range("L2").End(xlDown).Address
        ' Sets the range for the Max function
        Set rng = .Range("L2:" + lastrow)
        ' Gets the Max percent change
        pct_max = Application.WorksheetFunction.Max(rng)
        ' Formats the pct max value per specification
        pct = Format(pct_max, "0.##%")
    End With
    
    With ActiveSheet.Range("L:L")
        ' Block used to find the cell address for the max value
        Set c = .Find(pct, LookIn:=xlValues)
        If Not c Is Nothing Then
            cell_loc = c.Address
        End If
    End With
    ticker_Addr = cell_loc
    ' Get ticker address for the max value
    ticker_Addr = Replace(cell_loc, "L", "J")
    
    Cells(2, 17).Value = Range(ticker_Addr).Value
    Cells(2, 18).Value = Range(cell_loc).Value
    Cells(2, 18).NumberFormat = "0.00%"
    
End Sub

Sub findMindecrease()
    Dim lastrow As Variant
    Dim rng As Range
    Dim pct_min As Variant
    Dim cell_loc As String
    Dim c As Range
    Dim ticker_Addr As String
    Dim pct As Variant
    
    
    With ActiveSheet
        ' Finds the last cell in the column
        lastrow = .Range("L2").End(xlDown).Address
        ' Sets the range for the Max function
        Set rng = .Range("L2:" + lastrow)
        ' Gets the Min percent change
        pct_min = Application.WorksheetFunction.Min(rng)
        ' Formats the pct min value per specification
        pct = Format(pct_min, "0.00%")
    End With
    
    With ActiveSheet.Range("L:L")
        ' Block used to find the cell address for the max value
        Set c = .Find(pct, LookIn:=xlValues)
        If Not c Is Nothing Then
            cell_loc = c.Address
        End If
    End With
    ticker_Addr = cell_loc
    ' Get ticker address for the max value
    ticker_Addr = Replace(cell_loc, "L", "J")
    
    Cells(3, 17).Value = Range(ticker_Addr).Value
    Cells(3, 18).Value = Range(cell_loc).Value
    Cells(3, 18).NumberFormat = "0.00%"
    


End Sub
Sub findMaxStockVolume()
    Dim lastrow As Variant
    Dim rng As Range
    Dim stock_vol As Double
    Dim cell_loc As String
    Dim c As Range
    Dim ticker_Addr As String
    Dim pct As Variant
    
    
    With ActiveSheet
        ' Finds the last cell in the column
        lastrow = .Range("M2").End(xlDown).Address
        ' Sets the range for the Max function
        Set rng = .Range("M2:" + lastrow)
        ' Gets the Max stock volume
        stock_vol = Application.WorksheetFunction.Max(rng)
    End With
    
    With ActiveSheet.Range("M:M")
        ' Block used to find the cell address for the max value
        Set c = .Find(stock_vol, LookIn:=xlValues)
        If Not c Is Nothing Then
            cell_loc = c.Address
        End If
    End With
    ticker_Addr = cell_loc
    ' Get ticker address for the max value
    ticker_Addr = Replace(cell_loc, "M", "J")
    
    Cells(4, 17).Value = Range(ticker_Addr).Value
    Cells(4, 18).Value = Range(cell_loc).Value
    
End Sub

