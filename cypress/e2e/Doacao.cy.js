Cypress.Commands.add('deletePadrinhos', () => {
  cy.exec('python delete_padrinhos.py', { failOnNonZeroExit: false }).then((result) => {
    console.log(result.stdout);
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});

Cypress.Commands.add('cadastro', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.login-btn').click();
  cy.get('.register-link').click();
  cy.get('.btn-continue').click();
  cy.get('.btn-continue').click();
  cy.get('.btn-continue').click();
  cy.get('.btn-continue').click();
  cy.get('.btn-continue').click();
  cy.get('.btn-continue').click();
  cy.get('#username').type('teste');
  cy.get('#email').type('teste@example.com');
  cy.get('#password').type('123');
  cy.get('#password_confirm').type('123');
  cy.get('.btn-login').click();
  cy.get('#nome_completo').type('teste testavel');
  cy.get('#endereco').type('rua teste');
  cy.get('#pais').type('Brasil');
  cy.get('#cidade').type('Recife');
  cy.get('#numero_rua').type('00');
  cy.get('#complemento_rua').type('aaaaaaaaaa');
  cy.get('#telefone').type('99999999999');
  cy.get('#data_nascimento').type('1111-11-11');
  cy.get('.btn-login').click();
});

Cypress.Commands.add('login', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.login-btn').click();
  cy.get('#username').type('teste');
  cy.get('#password').type('123')
  cy.get('.btn-login').click();
});

Cypress.Commands.add('falha', () => {
  cy.get('.menu-buttons').click();
  cy.get(':nth-child(2) > :nth-child(1) > a').click();
  cy.get('[style="width: 30%; text-align: center;"] > a').click();
  cy.get('[onclick="mostrarMetodos()"]').click();
});

Cypress.Commands.add('sucesso', () => {
  cy.get('.menu-buttons').click();
  cy.get(':nth-child(2) > :nth-child(1) > a').click();
  cy.get('[style="width: 30%; text-align: center;"] > a').click();
  cy.get('#valor').type(2000);
  cy.get('[onclick="mostrarMetodos()"]').click();
  cy.get("[onclick=\"enviarDoacao('pix')\"]").click();
});

describe('fazer doação livre', () => {
  before(() => {
    cy.deletePadrinhos(); 
    // cy.cadastro();
  });


  it('Cenario 1: o usuario consegue efetuar a doação de forma correta', () => {
    cy.login();
    cy.sucesso();
  });

  it('Cenario 2: sucesso do apadrinhamento', () => {
    cy.login();
    cy.falha();
  });
})