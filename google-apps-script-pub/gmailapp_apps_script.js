//SCRIPT PARA EMAIL AUTOMÁTICO DE ADVERTÊNCIA AOS PILOTOS QUANDO PRÓXIMO DO VENCIMENTO DO CVI

let App = SpreadsheetApp
let Mail = GmailApp

let Spreadsheet = App.getActiveSpreadsheet()
let Sheet = Spreadsheet.getSheetByName('VALIDADE DOS CARTÕES')

let dateValues = Sheet.getRange('F3:F31').getValues()
let nameValues = Sheet.getRange('C3:C31').getValues()
let emailValues = Sheet.getRange('D3:D31').getValues()

let dateList = []
    dateValues.forEach((item)=>{dateList.push(item[0])})

let nameList = []
    nameValues.forEach((item)=>{nameList.push(item[0])})

let emailList = []
    emailValues.forEach((item)=>{emailList.push(item[0])})
  
let today = Math.round(new Date().getTime() / 86400000)

let subject ='REVALIDAÇÃO DE CVI'

let body = 'Por gentileza, providencie a revalidação de seu CVI o mais breve possível da seguinte forma:\n 1) Realize a prova teórica com aproveitamento mínimo de 80%, através do seguinte link: https://forms.gle/TZ9r6NdtRVeqd75w9\n 2) Realize um voo de cheque de CVI com um instrutor e assine virtualmente sua ficha de voo no SAGEM.\n 3) Informe a CCIAO por qualquer meio de comunicação quando da realização dos itens 1 e 2 para que seja iniciada a tramitação do processo no setor.\n Bons voos!'

function sentIf(){

  for (let i=0;i<dateValues.length;i++){
    
    let date = Math.round(dateList[i].getTime() / 86400000)

    let quota = MailApp.getRemainingDailyQuota()  
    
    if (date == today + 45){
      Mail.sendEmail(emailList[i],subject,'Olá '+nameList[i]+', seu CVI vencerá em 45 dias.'+body,{cc: "ceruttimcm@fab.mil.br,leonardodlm@fab.mil.br"})
      Mail.sendEmail('matheus.cerutti@hotmail.com','ENVIO DE EMAILS','Houve envio de email hoje para '+nameList[i]+',restando apenas '+quota+' emails.')
    } else if (date == today + 30) {
      Mail.sendEmail(emailList[i],subject,'Olá '+nameList[i]+', seu CVI vencerá em 30 dias.'+body,{cc: "ceruttimcm@fab.mil.br,leonardodlm@fab.mil.br"})
      Mail.sendEmail('matheus.cerutti@hotmail.com','ENVIO DE EMAILS','Houve envio de email hoje para '+nameList[i]+',restando apenas '+quota+' emails.')
    } else if (date == today + 15) {
      Mail.sendEmail(emailList[i],subject,'Olá '+nameList[i]+', seu CVI vencerá em 15 dias.'+body,{cc: "ceruttimcm@fab.mil.br,leonardodlm@fab.mil.br,mauriciomses@fab.mil.br,ramirorpf@fab.mil.br,ravilarapn@fab.mil.br"})
      Mail.sendEmail('matheus.cerutti@hotmail.com','ENVIO DE EMAILS','Houve envio de email hoje para '+nameList[i]+',restando apenas '+quota+' emails.')
    } else if (date == today + 7) {
      Mail.sendEmail(emailList[i],subject,'Olá '+nameList[i]+', seu CVI vencerá em 7 dias.'+body,{cc: "ceruttimcm@fab.mil.br,leonardodlm@fab.mil.br"})
      Mail.sendEmail('matheus.cerutti@hotmail.com','ENVIO DE EMAILS','Houve envio de email hoje para '+nameList[i]+',restando apenas '+quota+' emails.')
    }
  }
}

function sentNow(){

  for (let i=0;i<dateValues.length;i++){

    let quota = MailApp.getRemainingDailyQuota()  
    
    Mail.sendEmail(emailList[i],subject,'Olá '+nameList[i]+'.'+body,{cc: "ceruttimcm@fab.mil.br,leonardodlm@fab.mil.br"})
    Mail.sendEmail('matheus.cerutti@hotmail.com','ENVIO DE EMAILS','Houve envio de email hoje para '+nameList[i]+',restando apenas '+quota+' emails.') 
  }
}