select count(*) from client;
select * from client c, order o where c.idClient = o.idOrderClient;

select firstName, lastName, idOrder, orderStatus from client c, order o where c.idClient = o.idOrderClient;
select concat(firstName,' ', lastName) as fullname, idOrder as request, orderStatus from client c, order o where c.idClient = o.idOrderClient;

select count(*) from clients c, orders o where c.idClient = o.idOrderClient;

select * from clients c left outer join orders o on c.idClient = o.idOrderClient;

select * from clients c inner join orders o on c.idClient == o.idOrderClient;
                        inner join productOrder p on p.idOrder = o.idOrder
                        group by idClient


select * from client 
        order by firstName

