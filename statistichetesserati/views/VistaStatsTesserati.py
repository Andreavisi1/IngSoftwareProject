import datetime

from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QTableWidget, QListView, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

from statistichetesserati.controller.ControlloreStatsTesserati import ControlloreStatsTesserati
from math import ceil


class VistaStatsTesserati(QWidget):
    def __init__(self):
        super(VistaStatsTesserati, self).__init__()

        #self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)
        self.setFixedSize(625, 700)
        self.setWindowTitle(self.set_title())


    def set_title(self):
        return "Statistiche tesserati"







"""

#genera array vuoti da popolare con le informazioni del file pickle
        self.categoria = []
        self.quantita_categoria = []
        self.eventi = []

        self.chartview = QChartView()


        self.controllerstats = ControlloreStatsTesserati()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_total = QListView()


        self.create_pie(datascelta)
        self.populate_table(datascelta)
        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))
        self.table_widget.setMaximumHeight(200)


        self.v_layout.addWidget(self.chartview)
        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)


        self.setLayout(self.v_layout)
        self.setFixedSize(625, 700)
        self.setWindowTitle(self.set_title(datascelta))
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)

    #popola array con le informazioni dal file pickle e raggruppa gli eventi per categoria
    def build_pie(self, datascelta):
        for evento in self.controllerstats.get_lista_delle_stats():
            if evento.data_acquisto >= datascelta:
                j = 0
                for i in range(len(self.categoria)):
                    if self.categoria[i] == evento.categoria:
                        self.quantita_categoria[i] += evento.quantita_attivita
                        j = 1
                if j == 0:
                    self.categoria.append(evento.categoria)
                    self.quantita_categoria.append(evento.quantita_attivita)

    #popola array con le informazioni dal file pickle
    def build_table(self, datascelta):
        for evento in self.controllerstats.get_lista_delle_stats():
            if evento.data_acquisto >= datascelta:
                j = 0
                for product in self.eventi:
                    if product.id == evento.id:
                        product.quantita_attivita += evento.quantita_attivita
                        j = 1
                if j == 0:
                    self.eventi.append(evento)

    #genera il grafico a torta e lo popola utilizzando i dati dell' array
    def create_pie(self, data):
        series = QPieSeries()

        self.build_pie(data)

        if self.quantita_categoria == []:
            QMessageBox.critical(self, 'Errore', 'Nessuna statistica da visualizzare', QMessageBox.Ok, QMessageBox.Ok)
        else:

            try:

                slice = series.append(self.categoria[0], self.quantita_categoria[0])
                slice.setBrush(QtGui.QColor("#FF5631"))
                slice = series.append(self.categoria[1], self.quantita_categoria[1])
                slice.setBrush(QtGui.QColor("#31B1FF"))
                slice = series.append(self.categoria[2], self.quantita_categoria[2])
                slice.setBrush(QtGui.QColor("#31FF4D"))
                slice = series.append(self.categoria[3], self.quantita_categoria[3])
                slice.setBrush(QtGui.QColor("#DA31FF"))
                slice = series.append(self.categoria[4], self.quantita_categoria[4])
                slice.setBrush(QtGui.QColor("#FFEC31"))

            except IndexError:
                pass





        chart = QChart()
        font = QFont()
        font.setPointSize(18)
        chart.addSeries(series)
        chart.setTitleFont(font)
        chart.setTitle(self.set_title(data))

        self.chartview = QChartView(chart)
"""
"""
    #genera il titolo della pagina in base alla data passata dalla view precedente
    def set_title(self):


        return "Statistiche tesserati"
"""
"""

    #crea tabella contenente tutti gli eventi venduti registrati e la popola con i dati contenuti nell' array
    def populate_table(self, datascelta):

        self.build_table(datascelta)

        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.create_table(0, "Quantità")
        self.create_table(1, "Marca")
        self.create_table(2, "Nome Evento")
        self.create_table(3, "Categoria")

        prezzofinalecarrello = 0
        row = 0
        for evento in self.eventi:

            self.table_widget.insertRow(row)
            self.inserisci_elemento_in_tabella(evento.quantita_attivita, row, 0)
            self.inserisci_elemento_in_tabella(evento.marca, row, 1)
            self.inserisci_elemento_in_tabella(evento.nome, row, 2)
            self.inserisci_elemento_in_tabella(evento.categoria, row, 3)

            acquistototale = float(evento.quantita_attivita) * float(evento.prezzo)
            row = row + 1
            prezzofinaleattivita += float(acquistototale)

        self.table_total_model = QStandardItemModel(self.table_total)
        item = QStandardItem()
        prezzofinalecarrello = ceil(prezzofinalecarrello * 100) / 100.0
        item.setText("Totale: " + str(prezzofinalecarrello) + "€")
        item.setEditable(False)
        font = item.font()
        font.setPointSize(14)
        font.setBold(True)
        item.setFont(font)
        self.table_total_model.appendRow(item)
        self.table_total.setModel(self.table_total_model)

    #genera gli header della tabella contenenti gli eventi
    def create_table(self, index, label):

        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        item.setFont(font)
        item.setText(label)
        self.table_widget.setHorizontalHeaderItem(index, item)
        self.table_widget.setColumnWidth(index, 140)

    #inserisce un singolo elemento in una cella predefinita della tabella dato un indice
    def inserisci_elemento_in_tabella(self, elemento, row, index):
        item = QTableWidgetItem()
        item.setText(str(elemento))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.table_widget.setItem(row, index, item)
"""