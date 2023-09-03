-- criando banco de dados do exercios para ecommerce

create database ecommerce

use ecommerce

-- Criando as tabelas
create table client (
    idClient int auto_increment primary key,
    firstName varchar(10),
    mInit char(3),
    lastName varchar(20),
    cpf char(11) not null,
    clientAddress varchar(50)

    constraint unique_cpf_client unique (cpf)
);

alter table client auto_increment+1;


create table product(
    idProduct int auto_increment primary key,
    productName varchar(10),
    classification_kids bool default false, 
    category enum('Eletronico', "Vestimenta", "Brinquedos", "Alimentos", "Moveis") not null,
    evaluation float default 0, 
    size varchar(10)
);

alter table product auto_increment+1;

create table payment (
    idPaymentClient int, 
    idPayment int auto_increment,
    typePayment enum('Boleto', 'Cartão', 'Pix'),
    limitAvailable float,
    primary key(idClient, idPayment),

    constraint fk_payment_client foreign key (idPaymentClient) references client(idClient)
);

create table order (
    idOrder int auto_increment primary key,
    idOrderClient int, 
    orderStatus enum('Cancelado', "Confirmado", "Em processamento") default "Em processamento",
    oderDescription varchar(255),
    sendValue float default 10, 
    paymentCash boolean default false, 

    constraint fk_order_client foreign key (idOrderClient) references client(idClient)
        on update cascade
        on delete set null
);

alter table order auto_increment+1;

create table productStorage (
    idProductStorage int auto_increment primary key, 
    storageAddress varchar(255),
    quantity int default 0 
);

alter table productStorage auto_increment+1;


create table supplier (
    idSupplier int auto_increment primary key,
    socialName varchar(255) not null,
    cnpj char(15) not null,
    contact char(11) not null,
    
    constraint unique_cnpj_client unique (cnpj)
);

alter table supplier auto_increment+1;

create table seller (
    idSeller int auto_increment primary key,
    socialName varchar(255) not null,
    absName  varchar(255), 
    cnpj char(15),
    cpf char(11),
    sellerAddress varchar(255),
    contact char(11) not null,

    constraint unique_cnpj_client unique (cnpj),
    constraint unique_cpf_client unique (cpf)
);

alter table seller auto_increment+1;


create table productSupplier (
    idSupplier int, 
    idProduct int, 
    productQuantity int not null, 
    primary key (idProductSeller, idSupplier),

    constraint fk_productSupplier_supplier foreign key (idSupplier) references supplier(idSupplier),
    constraint fk_productSupplier_product foreign key (idProduct) references product(idProduct)
);

create table productSeller (
    idProductSeller int, 
    idProduct int, 
    productQuantity int default 1, 
    primary key (idProductSeller, idProduct),

    constraint fk_productSeller_seller foreign key (idProductSeller) references seller(idSeller),
    constraint fk_productSeller_product foreign key (idProduct) references product(idProduct)
);

create table productOrder (
    idProductOrder int, 
    idProduct int, 
    productQuantity int default 1,
    productOrderStatus enum('Disponivel', 'Sem estoque')  default Disponivel
    primary key (idProductOrder, idProduct),

    constraint fk_productOrder_order foreign key (idProductOrder) references order(idOrder),
    constraint fk_productOrder_product foreign key (idProduct) references product(idProduct)
);


create table storageLocation (
    idProduct int,
    idProductStorage int,
    sLocation varchar(255) not null,
    primary key (idProduct, idProductStorage),

    constraint fk_storageLocation_storage foreign key (idProductStorage) references productStorage(idProductStorage),
    constraint fk_storageLocation_product foreign key (idProduct) references product(idProduct)
);

show tables;



