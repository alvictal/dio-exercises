use ecommerce

insert into client (firstName, mInit, lastName, cpf, clientAddress)
            values  ('Maria', 'M', 'Silva', 12345678910, 'Rua das flores'),
                    ('João', 'P', 'Pimentel', 10123456789, 'Rua das Arvores'),
                    ('Pedro', 'J', 'Oliveira', 89101234567, 'Rua das Montanhas'),
                    ('Julia', 'A', 'Mascarenhas', 89671012345, 'Rua dos Lirios'),
                    ('Aluisio', 'L', 'Victal', 11123456789, 'Rua Jose Pelino'),
                    ('Kamila', 'L', 'Silva', 11333456789, 'Rua Roberto Augusto');



insert into product (productName, classification_kids, category, evaluation, size) 
            values  ('Fone de Ouvido', false, 'Eletronico','4', null),
                    ('Barbie', true, 'Brinquedos', '3', null),
                    ('Camiseta', false, 'Vestimenta', '5', null),
                    ('Microfone', false, 'Eletronico','4', null);


insert into orders (idOrderClient, orderStatus, oderDescription, sendValue, paymentCash)
            values  (1, default, 'Compra via aplicativo', null, true),
                    (2, default, 'Compra via aplicativo', 50, false),
                    (3, 'Confirmado', null, null, true),
                    (4, default, 'Compra via web site', 150, false);

insert into productOrder (idProductOrder, idProduct, productQuantity, productOrderStatus)
            values  (1,1,2, null),
                    (2,1,2, null),
                    (3,1,2, null);


insert into productStorage(storageAddress, quantity)
            values  ('Rio de Janeiro', 1000),
                    ('Rio de Janeiro', 500),
                    ('São Paulo', 10),
                    ('São Paulo', 100),
                    ('São Paulo', 1000),
                    ('Belo Horizonte', 60);


insert into storageLocation (idProduct, idProductStorage, sLocation)
            values  (1,2,'RJ'),
                    (2,4,'SP');

insert into supplier (socialName, cnpj, contact)
            values  ('Jose e filhos', '1234567890098', '123456789')
                    ('Eletronicos filhos', '3456789009812', '123456710')
                    ('Eletronicos jose', '1256789009812', '123456778');

insert into productSupplier (idSupplier, idProduct, quantity)
            values  (1,1,500),
                    (1,2,400),
                    (2,3,600),
                    (3,4,100);

insert into seller (socialName, absName, cnpj, cpf, sellerAddress, contact)
            values  ('Tech Eletronics', null, 1321456789189, null, 'Rio de Janeiro', 2198781029),
                    ('Vestimentas Ze', null, null, 671234560989, 'Rio de Janeiro', 2198781021),
                    ('PlayKids', null, 1321456789180, null, 'São Paulo', 1198781021);

insert into productSeller(idSeller, idProduct, productQuantity)
            values  (1,4,80),
                    (2,3,10);