Cypress.Commands.add('deletePadrinhos', () => {
  cy.exec('python delete_padrinhos.py', { failOnNonZeroExit: false }).then((result) => {
    console.log(result.stdout);
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});

Cypress.Commands.add('deleteCartas', () => {
  cy.exec('python delete_cartas.py', { failOnNonZeroExit: false }).then((result) => {
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
  cy.get(':nth-child(1) > :nth-child(3) > a').click();
  cy.get(':nth-child(2) > a > div').click();
  cy.get('[type="text"]').type('teste');
  cy.get('textarea').type('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
  cy.get('button').click();
});

Cypress.Commands.add('sucesso', () => {
  cy.get('.menu-buttons').click();
  cy.get(':nth-child(1) > :nth-child(3) > a').click();
  cy.get(':nth-child(2) > a > div').click();
  cy.get('[type="text"]').type('teste');
  cy.get('textarea').type('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
  cy.get('select').select(1);
  cy.get('button').click();
  
});

describe('fazer doação livre', () => {
  before(() => {
    cy.deletePadrinhos(); 
    cy.deleteCartas(); 
    cy.cadastro();
  });


  it('Cenario 1: o usuario consegue enviar uma carta para o apadrinhado respectivo', () => {
    cy.login();
    cy.sucesso();
  });

  it('Cenario 2: falha no envio por erro de formatação', () => {
    cy.login();
    cy.falha();
  });
})