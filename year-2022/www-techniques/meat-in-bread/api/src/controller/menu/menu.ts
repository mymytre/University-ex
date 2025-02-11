import express, {Request, Response} from 'express';
import {Menu} from '../../model/menu';

const router = express.Router();

router.get(
    '/api/menu',
    async (req: Request, res: Response) => {
        const menu = await Menu.find();
        res.status(200).send(menu);
    }
);

export {router as meatMenu};
