Cypress.Commands.add('deleteSuperusers', () => {
  cy.exec('python scriptsTestes\\delete_superusers.py', { failOnNonZeroExit: false }).then((result) => {
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

Cypress.Commands.add('postagem', () => {
  cy.visit('http://127.0.0.1:8000/adm/home/');
  cy.get('[href="/adm/gerenciar-feed/"]').click();
  cy.get('.add-button').click();
  cy.get('#titulo').type(`teste`);
  cy.get('#conteudo').type(`teste`);
  cy.get('.sidebar > .action-button-bottom').click();
});

Cypress.Commands.add('excluir', () => {
  cy.visit('http://127.0.0.1:8000/adm/home/');
  cy.get('[href="/adm/gerenciar-feed/"]').click();
  cy.get(':nth-child(1) > .post-right > .manage-post-button').click();
  cy.get('.button-delete').click();
  
});

Cypress.Commands.add('editar', () => {
  cy.visit('http://127.0.0.1:8000/adm/home/');
  cy.get('[href="/adm/gerenciar-feed/"]').click();
  cy.get(':nth-child(1) > .post-right > .manage-post-button').click();
  cy.get('.primary-input-field').clear().type('teste2');
  cy.get('.textarea-full-width').clear().type('teste2');
  cy.get('.button-save').click();
  
});




describe('Gerenciar Feed', () => {
  before(() => {
    return cy.deleteSuperusers()
      .then(() => cy.createSuperuser())
  });


  it('Cenario 1: Criar uma postagem', () => {
    // cy.loginAdmin();
    cy.postagem();
  });

  it('Cenario 2: Editar um poste', () => {
    // cy.loginAdmin();
    cy.editar();
  });

  it('Cenario 3: Excluir um poste', () => {
    // cy.loginAdmin();
    cy.excluir();
  });

});