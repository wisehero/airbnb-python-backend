import React from 'react';
import ReactDOM from 'react-dom/client';
import {ChakraProvider} from "@chakra-ui/react";
import {RouterProvider} from "react-router-dom";
import router from "./router";


const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <ChakraProvider>
            <RouterProvider router={router}></RouterProvider>
        </ChakraProvider>
    </React.StrictMode>
);
