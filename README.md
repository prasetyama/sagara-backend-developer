## Run

Git Clone

type this command to run:

```Shell
git clone https://github.com/prasetyama/simple-rent-mobil.git
```

```Shell
composer update
```

Create file .env and change with your database config

```Shell
cp .env.example .env
```

Created Database

Migrate Database

```Shell
php artisan migrate
```

Create Role Permission with run this command
```Shell
php artisan permission:create-permission-routes
```

Add user admin Seeder
```Shell
php artisan db:seed --class=CreateAdminUserSeeder
```

## Run this Project
```Shell
php artisan serve
```
