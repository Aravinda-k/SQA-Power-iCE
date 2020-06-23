class EmpowerLoginDialogClass():

  def __init__(self):
    self.empowerLoginDialog = Aliases.Empower.Empower_LoginDialog
    self.advancedBtn = Aliases.Empower.Empower_LoginDialog.Advanced_Button
    self.cancelBtn = Aliases.Empower.Empower_LoginDialog.Cancel_Button
    self.comboBox = Aliases.Empower.Empower_LoginDialog.ComboBox
    self.helpBtn = Aliases.Empower.Empower_LoginDialog.Help_Button
    self.okBtn = Aliases.Empower.Empower_LoginDialog.OK_Button
    self.passwordEditField = Aliases.Empower.Empower_LoginDialog.Password_EditField
    self.usernameEditField = Aliases.Empower.Empower_LoginDialog.Username_EditField
    
  def empowerLogin(self):
    if TestedApps.Empower.Count > 0:
      
      self.usernameEditField.SetText(Project.Variables.empowerUsername)
      self.passwordEditField.SetText(Project.Variables.empowerPassword)
      self.okBtn.Click()
    else:
      Log.Message("Empower Application has not been Launched, Please launch Empower before login")
  
  def invokeEmpowerApp(self):
    TestedApps.Empower.Run(1, True)