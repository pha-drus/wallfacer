Attribute VB_Name = "Module2"
Sub stocks_summary()
' Create a script that will loop through all the stocks for one year and output the following information:

' - The ticker symbol.

' - Yearly change from opening price at the beginning of a given year to the closing price at the end of that year.

' - The percent change from opening price at the beginning of a given year to the closing price at the end of that year.

' - The total stock volume of the stock.

' -----------------------------------------------------------------------------------

Dim sheet As Worksheet

Dim book As Workbook
    
    Set book = ActiveWorkbook


MsgBox ("Click OK to begin. This may take a minute or two.")

For Each sheet In Worksheets

  sheet.Range("J1").Value = "Ticker Symbol"
  sheet.Range("J1").Font.Bold = True
  sheet.Range("K1").Value = "Yearly Change"
  sheet.Range("K1").Font.Bold = True
  sheet.Range("L1").Value = "Percent Change"
  sheet.Range("L1").Font.Bold = True
  sheet.Range("M1").Value = "Total Stock Volume"
  sheet.Range("M1").Font.Bold = True

  Dim ticker_symbol As String

  Dim yearly_change As Double
  
  Dim opening_price As Double
  
  Dim percent_change As String
  
  Dim total_volume As Double
  total_volume = 0

  Dim summarytablerow As Integer
  summarytablerow = 2
  
  bottom = sheet.Cells(Rows.Count, 1).End(xlUp).Row
  
  opening_price = sheet.Cells(2, 3).Value
  
  For I = 2 To bottom
  
    If sheet.Cells(I + 1, 1).Value <> sheet.Cells(I, 1).Value Then
    
      closing_price = sheet.Cells(I, 6).Value

      ticker_symbol = sheet.Cells(I, 1).Value

      total_volume = total_volume + sheet.Cells(I, 7).Value
      
      yearly_change = closing_price - opening_price

      sheet.Range("J" & summarytablerow).Value = ticker_symbol

      sheet.Range("K" & summarytablerow).Value = yearly_change
      
      If (yearly_change > 0) Then
                    sheet.Range("K" & summarytablerow).Interior.ColorIndex = 4
                    
                ElseIf (Yearly_Price_Change <= 0) Then
                
                    sheet.Range("K" & summarytablerow).Interior.ColorIndex = 3
                End If
      
      ' Percent change:
        
        If opening_price = 0 Then
        
            sheet.Range("L" & summarytablerow).Value = (sheet.Cells(I, 6).Value - opening_price) / 0.01
        Else
      
            sheet.Range("L" & summarytablerow).Value = (sheet.Cells(I, 6).Value - opening_price) / opening_price
            
        End If


      sheet.Range("M" & summarytablerow).Value = total_volume


      summarytablerow = summarytablerow + 1
      
      opening_price = sheet.Cells(I + 1, 3).Value
      
      total_volume = 0

    Else

      total_volume = total_volume + sheet.Cells(I, 7).Value
      
      
      
      

    End If

  Next I


sheet.Columns("L").NumberFormat = "0.00%"

Next sheet

MsgBox ("Process Complete")

End Sub
