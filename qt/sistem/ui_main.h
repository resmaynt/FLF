/********************************************************************************
** Form generated from reading UI file 'mainWindowLrafjd.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINWINDOWLRAFJD_H
#define MAINWINDOWLRAFJD_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_mainWindow
{
public:
    QLabel *label;
    QPushButton *pushButton;
    QLineEdit *fileLineEdit;
    QPushButton *pushButton_2;
    QLineEdit *fileLineEdit_2;
    QPushButton *pushButton_3;

    void setupUi(QDialog *mainWindow)
    {
        if (mainWindow->objectName().isEmpty())
            mainWindow->setObjectName(QStringLiteral("mainWindow"));
        mainWindow->resize(1020, 610);
        mainWindow->setStyleSheet(QLatin1String("#mainWindow {\n"
"    border-image: url(:/img/2.jpg) 0 0 0 0 stretch stretch;\n"
"}\n"
"QWidget#mainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0.274, y1:0.295, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
""));
        label = new QLabel(mainWindow);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(210, 20, 661, 91));
        label->setStyleSheet(QLatin1String("\n"
"	font: 600 28pt \"Segoe UI\";color:rgb(255, 255, 255)"));
        pushButton = new QPushButton(mainWindow);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(440, 340, 131, 41));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton->sizePolicy().hasHeightForWidth());
        pushButton->setSizePolicy(sizePolicy);
        QFont font;
        font.setFamily(QStringLiteral("Segoe UI"));
        font.setPointSize(12);
        font.setBold(true);
        font.setItalic(false);
        font.setWeight(75);
        pushButton->setFont(font);
        pushButton->setStyleSheet(QString::fromUtf8("\n"
"/* Base */\n"
"QPushButton {\n"
"    border-radius: 15px;\n"
"    border: 1px solid transparent;   /* biar ukuran tidak loncat */\n"
"	/* contoh: teks terasa sedikit turun \342\206\222 angkat 1px */\n"
"	padding-bottom: 3px; \n"
"\n"
"	font: 600 12pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(49, 99, 148);   /* #316394 */\n"
"}\n"
"\n"
"/* Muncul border hanya ketika ditekan */\n"
"QPushButton:pressed {\n"
"    border-color: #888;\n"
"    background-color: rgb(44, 88, 132);   /* sedikit lebih gelap */\n"
"}\n"
"\n"
"/* Jika mau juga saat di-hover, buka komentar di bawah */\n"
"// QPushButton:hover {\n"
"//     border-color: #888;\n"
"// }\n"
""));
        fileLineEdit = new QLineEdit(mainWindow);
        fileLineEdit->setObjectName(QStringLiteral("fileLineEdit"));
        fileLineEdit->setGeometry(QRect(320, 190, 331, 41));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(fileLineEdit->sizePolicy().hasHeightForWidth());
        fileLineEdit->setSizePolicy(sizePolicy1);
        fileLineEdit->setStyleSheet(QLatin1String("QLineEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"border-radius: 5px;"));
        fileLineEdit->setClearButtonEnabled(true);
        pushButton_2 = new QPushButton(mainWindow);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(660, 190, 71, 41));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(pushButton_2->sizePolicy().hasHeightForWidth());
        pushButton_2->setSizePolicy(sizePolicy2);
        pushButton_2->setMouseTracking(false);
        pushButton_2->setAutoFillBackground(false);
        pushButton_2->setStyleSheet(QLatin1String("/* Base */\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid transparent;   /* biar ukuran tidak loncat */\n"
"    padding: 4px;\n"
"\n"
"\n"
"	font: 600 8pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(49, 99, 148);   /* #316394 */\n"
"}\n"
"\n"
"/* Muncul border hanya ketika ditekan */\n"
"QPushButton:pressed {\n"
"    border-color: #888;\n"
"    background-color: rgb(44, 88, 132);   /* sedikit lebih gelap */\n"
"}\n"
"\n"
"/* Jika mau juga saat di-hover, buka komentar di bawah */\n"
"// QPushButton:hover {\n"
"//     border-color: #888;\n"
"// }\n"
""));
        pushButton_2->setCheckable(false);
        fileLineEdit_2 = new QLineEdit(mainWindow);
        fileLineEdit_2->setObjectName(QStringLiteral("fileLineEdit_2"));
        fileLineEdit_2->setGeometry(QRect(320, 250, 331, 41));
        sizePolicy1.setHeightForWidth(fileLineEdit_2->sizePolicy().hasHeightForWidth());
        fileLineEdit_2->setSizePolicy(sizePolicy1);
        fileLineEdit_2->setStyleSheet(QLatin1String("QLineEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"border-radius: 5px;"));
        fileLineEdit_2->setClearButtonEnabled(true);
        pushButton_3 = new QPushButton(mainWindow);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(660, 250, 71, 41));
        sizePolicy2.setHeightForWidth(pushButton_3->sizePolicy().hasHeightForWidth());
        pushButton_3->setSizePolicy(sizePolicy2);
        pushButton_3->setStyleSheet(QLatin1String("/* Base */\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid transparent;   /* biar ukuran tidak loncat */\n"
"    padding: 4px;\n"
"\n"
"   \n"
"	font: 600 8pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(49, 99, 148);   /* #316394 */\n"
"}\n"
"\n"
"/* Muncul border hanya ketika ditekan */\n"
"QPushButton:pressed {\n"
"    border-color: #888;\n"
"    background-color: rgb(44, 88, 132);   /* sedikit lebih gelap */\n"
"}\n"
"\n"
"/* Jika mau juga saat di-hover, buka komentar di bawah */\n"
"// QPushButton:hover {\n"
"//     border-color: #888;\n"
"// }\n"
""));

        retranslateUi(mainWindow);

        QMetaObject::connectSlotsByName(mainWindow);
    } // setupUi

    void retranslateUi(QDialog *mainWindow)
    {
        mainWindow->setWindowTitle(QApplication::translate("mainWindow", "Dialog", nullptr));
        label->setText(QApplication::translate("mainWindow", "Complete the Required Data", nullptr));
        pushButton->setText(QApplication::translate("mainWindow", "Submit", nullptr));
        fileLineEdit->setPlaceholderText(QApplication::translate("mainWindow", "FLF Report Data", nullptr));
        pushButton_2->setText(QApplication::translate("mainWindow", "browser", nullptr));
        fileLineEdit_2->setPlaceholderText(QApplication::translate("mainWindow", "Draft Power BI", nullptr));
        pushButton_3->setText(QApplication::translate("mainWindow", "browser", nullptr));
    } // retranslateUi

};

namespace Ui {
    class mainWindow: public Ui_mainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINWINDOWLRAFJD_H
