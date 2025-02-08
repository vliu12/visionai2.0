import React, {useEffect, useState} from 'react'
import api from '../api/api'

export const stopDetection = () => {
    try {
        const response = api.get('/stopClassify')
    } catch (error) {
        console.error("Error fetching", error.message)
    }
}