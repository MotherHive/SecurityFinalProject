GOALS:
If you're reading this, I'm going to take the chance to learn a few things with this project.
1. Full security testing and knowledge of my application. (Something, I'm not super well-versed in. I have the fundamentals.)
2. Proper Git workflow including no lazy messages and branches. 


TODO
- [x] Using SQLAlchemy query to avoid SQL Injection Attacks
- [x] Using python-env to avoid secrets and credentials out of source code 
- [x] Authentication that handles password safely (bcrypt hashing)
- [x] Input Validation (so far)
- [ ] Authentication logging
- [ ] Logout button
- [ ] Enforce NIST SP 800-63B 
- [ ] No direct database access
- [ ] Safe error handling that does not reveal infrastructure (including password errors)
- [ ] env.example and env error handling
- [ ] Output encoding
- [ ] Database population for USERS, PRODUCTS, ORDERS, ORDERS_ITEMS
- [ ] Order viewing and editing
- [ ] Admin locked registration
- [ ] User table permissions and implementation
- [ ] Access control layer with multiple enforced roles (ADMIN, WAREHOUSE_STAFF, MANAGER)
- [ ] Database setup scripts
- [ ] README start-up instructions + Env creation



BONUS
- [x] CSRF Protection


ROLES & PERMISSIONS:
ADMIN -> User creation, User deletion, Role changes, View orders
WAREHOUSE STAFF -> Change low-level order status, View orders
MANAGER -> Change all order status (including confirm), view orders