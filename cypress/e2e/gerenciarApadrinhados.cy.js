Cypress.Commands.add('deleteSuperusers', () => {
  cy.exec('python delete_superusers.py', { failOnNonZeroExit: false }).then((result) => {
    console.log(result.stdout);
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});

Cypress.Commands.add('createSuperuser', () => {
  cy.exec('python create_superuser.py', { failOnNonZeroExit: false }).then((result) => {
    console.log(result.stdout);
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});

const projectRoot = process.cwd();

Cypress.Commands.add('deleteApadrinhados', () => {
  cy.exec('python manage.py delete_apadrinhados', {
    failOnNonZeroExit: false,
    cwd: projectRoot
  }).then((result) => {
    console.log(result.stdout);
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});


Cypress.Commands.add('loginAdmin', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.getCookie('csrftoken').should('exist');
  cy.get('.adm-btn').click();
  cy.get('#id_username').type('admin');
  cy.get('#id_password').type('admin123');
  cy.get('form > button').click();
});



Cypress.Commands.add('falha', () => {
  cy.visit('http://127.0.0.1:8000/adm/home/');
  cy.get('[href="/adm/gerenciar-afilhados/"]').click();
  cy.get('[href="/afilhados/novo/"]').click();
  cy.get('button').click();
});

Cypress.Commands.add('sucesso', () => {
  cy.visit('http://127.0.0.1:8000/adm/home/');
  cy.get('[href="/adm/gerenciar-afilhados/"]').click();
  cy.get('[href="/afilhados/novo/"]').click();
  cy.get('#nome').type('teste');
  cy.get('#data_nascimento').type('1111-11-11');
  cy.get('#endereco').type('rua de teste');
  cy.get('button').click();
});

describe('Gerenciar Apadrinhados', () => {
  before(() => {
    return cy.deleteSuperusers()
      .then(() => cy.createSuperuser())
      .then(() => cy.deleteApadrinhados());
  });


  it('Cenario 1: Falha no Cadastramento devido a Campos Não Preenchidos Corretamente', () => {
    cy.loginAdmin();
    cy.falha();
  });

  it('Cenario 2: Sucesso no Cadastramento de um Apadrinhado', () => {
    cy.loginAdmin();
    cy.sucesso();
  });

});