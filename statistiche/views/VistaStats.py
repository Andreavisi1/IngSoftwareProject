import datetime

from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QTableWidget, QListView, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

from listatesserati.controller.ControlloreListaTesserati import ControlloreListaTesserati
from statistiche.controller.ControlloreStats import ControlloreStats
from math import ceil


class VistaStats(QWidget):
    def __init__(self):
        super(VistaStats, self).__init__()
       # self.datascelta = datascelta

#genera array vuoti da popolare con le informazioni del file pickle
        self.categoria = []
        self.quantita_categoria = []
        self.eventi = []

        self.tesserati = []
        self.gare_partecipate_tot = 0
        self.gare_vinte_tot = 0

        self.chartview = QChartView()

        self.controllerstats = ControlloreStats()
        self.controllertesserati = ControlloreListaTesserati()
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))

        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_partecipate = QListView()
        self.table_vinte = QListView()

        self.create_pie()
        self.populate_table()
        self.table_partecipate.setMaximumHeight(self.table_partecipate.sizeHintForRow(0))
        self.table_vinte.setMaximumHeight(self.table_vinte.sizeHintForRow(0))
        self.table_widget.setMaximumHeight(200)



        self.v_layout.addWidget(self.chartview)
        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_partecipate)
        self.v_layout.addWidget(self.table_vinte)

        self.setLayout(self.v_layout)
        self.setFixedSize(625, 700)
        self.setWindowTitle(self.set_title())
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)

    #popola array con le informazioni dal file pickle e raggruppa gli eventi per categoria
    def build_pie(self):
        for tesserato in self.controllertesserati.get_lista_dei_tesserati():
            j = 0
            for i in range(len(self.categoria)):
                if self.categoria[i] == tesserato.categoria:
                    self.quantita_categoria[i] += tesserato.gare_vinte
                    j = 1
            if j == 0:
                self.categoria.append(tesserato.categoria)
                self.quantita_categoria.append(tesserato.gare_vinte)

        """for evento in self.controllerstats.get_lista_delle_stats():
            j = 0
            for i in range(len(self.categoria)):
                if self.categoria[i] == evento.categoria:
                    self.quantita_categoria[i] += evento.quantita_attivita
                    j = 1
            if j == 0:
                self.categoria.append(evento.categoria)
                self.quantita_categoria.append(evento.quantita_attivita)"""

    #popola array con le informazioni dal file pickle
    def build_table(self):
        for tesserato in self.controllertesserati.get_lista_dei_tesserati():
            self.gare_partecipate_tot += int(tesserato.gare_partecipate)
            self.gare_vinte_tot += int(tesserato.gare_vinte)
            self.tesserati.append(tesserato)


        """for evento in self.controllerstats.get_lista_delle_stats():
            if evento.data_acquisto >= datascelta:
                j = 0
                for product in self.eventi:
                    if product.id == evento.id:
                        product.quantita_attivita += evento.quantita_attivita
                        j = 1
                if j == 0:
                    self.eventi.append(evento)"""

    #genera il grafico a torta e lo popola utilizzando i dati dell' array
    def create_pie(self):
        series = QPieSeries()

        self.build_pie()

        if self.quantita_categoria == []:
            QMessageBox.critical(self, 'Errore', 'Nessuna statistica da visualizzare', QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                print(self.categoria[0])
                print(self.quantita_categoria[0])
                slice = series.append(self.categoria[0], int(self.quantita_categoria[0]))
                slice.setBrush(QtGui.QColor("#FF5631"))
                slice = series.append(self.categoria[1], int(self.quantita_categoria[1]))
                slice.setBrush(QtGui.QColor("#31B1FF"))
                slice = series.append(self.categoria[2], int(self.quantita_categoria[1]))
                slice.setBrush(QtGui.QColor("#31FF4D"))
                slice = series.append(self.categoria[3], int(self.quantita_categoria[1]))
                slice.setBrush(QtGui.QColor("#DA31FF"))
                slice = series.append(self.categoria[4], int(self.quantita_categoria[1]))
                slice.setBrush(QtGui.QColor("#FFEC31"))

            except IndexError:
                pass

        chart = QChart()
        font = QFont()
        font.setPointSize(18)
        chart.addSeries(series)
        chart.setTitleFont(font)
        chart.setTitle("Gare vinte per categoria")

        self.chartview = QChartView(chart)

    #genera il titolo della pagina in base alla data passata dalla view precedente
    def set_title(self):

        return "Statistiche globali tesserati"

    #crea tabella contenente tutti gli eventi venduti registrati e la popola con i dati contenuti nell' array
    def populate_table(self):

        self.build_table()

        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.create_table(0, "Id Tesserato")
        self.create_table(1, "Categoria")
        self.create_table(2, "Gare Partecipate")
        self.create_table(3, "Gare Vinte")

        prezzofinalecarrello = 0
        row = 0
        for tesserato in self.tesserati:

            self.table_widget.insertRow(row)
            self.inserisci_elemento_in_tabella(tesserato.id, row, 0)
            self.inserisci_elemento_in_tabella(tesserato.categoria, row, 1)
            self.inserisci_elemento_in_tabella(tesserato.gare_partecipate, row, 2)
            self.inserisci_elemento_in_tabella(int(tesserato.gare_vinte), row, 3)
# Metodo Qt che ordina in maniera decrescente i tesserati in base al numero di gare vinte
    #        self.table_widget.sortItems(3, Qt.DescendingOrder)
    #        self.table_widget.sortItems(1, Qt.DescendingOrder)

        """acquistototale = float(evento.quantita_attivita) * float(evento.prezzo)
        row = row + 1
        prezzofinalecarrello += float(acquistototale)"""

        self.table_partecipate_model = QStandardItemModel(self.table_partecipate)
        self.table_vinte_model = QStandardItemModel(self.table_vinte)

        item_p = QStandardItem()
        item_p.setText("Gare partecipate totali: " + str(self.gare_partecipate_tot))
        item_p.setEditable(False)
        font = item_p.font()
        font.setPointSize(14)
        font.setBold(True)
        item_p.setFont(font)

        item_v = QStandardItem()
        item_v.setText("Gare vinte totali: " + str(self.gare_vinte_tot))
        item_v.setEditable(False)
        font = item_v.font()
        font.setPointSize(14)
        font.setBold(True)
        item_v.setFont(font)

        self.table_partecipate_model.appendRow(item_p)
        self.table_partecipate.setModel(self.table_partecipate_model)

        self.table_vinte_model.appendRow(item_v)
        self.table_vinte.setModel(self.table_vinte_model)

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

